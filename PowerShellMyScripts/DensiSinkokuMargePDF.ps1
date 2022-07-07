function check {
    param([array]$filePaths)
  
    $wsobj = new-object -comobject wscript.shell

    # check args exist
    if(!$filePaths){
        #$wsobj.popup("Please input FilePath at args[0].") | Out-Null
        Out-Null
        return $false
    }

    # check path length
    if($filePaths.Length -lt 2){
        #$wsobj.popup("Please input at least two FilePaths.") | Out-Null
        Out-Null
        return $false
    }

    # check path exist
    foreach($filePath in $filePaths) {
        if(!($filePath | test-path)) {
            #$wsobj.popup("Please input correct FilePath.`r`n'$($filePath)' does not exist.") | Out-Null
            Out-Null
            return $false
        }
    }

    # check file is PDF
    foreach($filePath in $filePaths) {
        if([System.IO.Path]::GetExtension($filePath) -ne ".pdf"){
            #$wsobj.popup("Please input PDF File.`r`n'$($filePath)' is not PDF.") | Out-Null
            Out-Null
            return $false
        }
    }

    return $true
}
function join {
    param(
        [array]$filePaths
    )

    if(check $filePaths){
        # sort filePaths
        $filePaths = $filePaths | sort
        # convert FilePath
        $files = @()
        foreach($filePath in $filePaths){
            $files += Convert-Path $filePath
        }
        # conbine PDF
        $inputFiles = $null
        foreach($file in $files){
            if($inputFiles -eq $null){
                $inputFiles = """" + $file + """"
            }else{
                #$inputFiles = "$inputFiles $file"
                $inputFiles = "$inputFiles """ + $file + """"
            }
        }
        $outputFile = """"+(Split-Path $filePaths[0] -Parent) + "\" +  ([System.IO.Path]::GetFileNameWithoutExtension((Split-Path $filePaths[0] -Leaf))) + "_merged.pdf"+""""
        $cmd = "pdftk $inputFiles cat output $outputFile"
        #$cmd = "pdftk $inputFiles cat output $outputFile"
        Invoke-Expression $cmd
    }
    #join $args    
}
function LoopMerged {
    param(
        [string]$path
    )
# 指定されたパス配下のファイルを取得
$target = Get-Childitem $path | Where-Object {-not $_.PSIsContainer}
$Wtarget = Get-Childitem $path | Where-Object {-not $_.PSIsContainer}
# WSHのShellオブジェクトを生成
$shell = New-Object -Com Shell.Application
$Wshell = New-Object -Com Shell.Application
# ファイル分だけ繰り返す
foreach ($item in $target){
    # GetDetailsOfに必要なオブジェクト
    $array = $item.Name.Split("_")
    $Flag = 0
    #$Wtarget | ForEach-Object {
        foreach ($Witem in $Wtarget){
        # GetDetailsOfに必要なオブジェクト
        $Warray = $Witem.Name.Split("_")
        if($item.FullName -ne $Witem.FullName) {
            if($array[0] -eq $Warray[0]) {

                join $item.FullName,$Witem.FullName
                Remove-Item -Path ($item.FullName)
                Remove-Item -Path ($Witem.FullName)
                $Flag = 1
                break
            }
            
        }
    }
    if($Flag -eq 1){
        break
        $Flag = 0
    }    
}
}

$Ys = Get-Date -Format "yyyy"
$Mo = Get-Date -Format "MM"
###################################################################################$Mo = $Mo - 1
$path = "\\Sv05121a\e\電子ファイル\メッセージボックス\" + $Ys + "-" + $Mo + "\送信分受信通知"####\TEST"
$Maintarget = Get-Childitem $path | Where-Object {-not $_.PSIsContainer}
for($i=0; $i -le $Maintarget.length; $i++) {
    LoopMerged $path
}
    # ファイル出力
    #$_.name + "`," + $folderobj.GetDetailsOf($item,148) | Add-Content $output
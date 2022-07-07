function GetDiffData($baseFilePath, $compFilePath) {
    $diffResult = Compare-Object $baseFilePath $compFilePath -IncludeEqual

    $diffBaseData = @()
    $diffCompData = @()
    $matchData = @()
    if(($diffResult -ne $null) -and ($diffResult.Count -gt 0)) {
        foreach($data in $diffResult) {
            $indicator = $data.SideIndicator
            $inputObject = $data.InputObject

            if($indicator -eq "<=") {
                # BaseFile.csvに存在し、CompFile.csvには存在しないデータ
                $diffBaseData += $inputObject
            } elseif ($indicator -eq "=>") {
                # CompFile.csvに存在し、BaseFile.csvには存在しないデータ
                $diffCompData += $inputObject
            } elseif ($indicator -eq "==") {
                # CompFile.csv、BaseFile.csv両方に存在するデータ
                $matchData += $inputObject
            } else {
                Write-Host "Invalid Line"
            }
        }

        return $diffBaseData, $diffCompData, $matchData
    }
}
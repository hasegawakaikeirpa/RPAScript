#Load SharePoint CSOM Assemblies
Add-Type -Path "C:\Program Files\PackageManagement\NuGet\Packages\Microsoft.SharePointOnline.CSOM.16.1.21012.12000\lib\net40-full\Microsoft.SharePoint.Client.dll"
Add-Type -Path "C:\Program Files\PackageManagement\NuGet\Packages\Microsoft.SharePointOnline.CSOM.16.1.21012.12000\lib\net40-full\Microsoft.SharePoint.Client.Runtime.dll"
 
#Variables for Processing

$WebUrl = "https://hasegawakaikeirpa.sharepoint.com/sites/msteams_d42518"
$LibraryName ="Documents"
$SourceFile="D:\SharePointLink.xlsm"
$AdminName ="hasegawarpa@hasegawakaikeirpa.onmicrosoft.com"
$AdminPassword ="HaseK5121"
  
#Setup Credentials to connect
$Credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($AdminName,(ConvertTo-SecureString $AdminPassword -AsPlainText -Force))
  
#Set up the context
$Context = New-Object Microsoft.SharePoint.Client.ClientContext($WebUrl)
$Context.Credentials = $Credentials
 
#Get the Library
$Library =  $Context.Web.Lists.GetByTitle($LibraryName)
 
#Get the file from disk
$FileStream = ([System.IO.FileInfo] (Get-Item $SourceFile)).OpenRead()
#Get File Name from source file path
$SourceFileName = Split-path $SourceFile -leaf
   
#sharepoint online upload file powershell
$FileCreationInfo = New-Object Microsoft.SharePoint.Client.FileCreationInformation
$FileCreationInfo.Overwrite = $true
$FileCreationInfo.ContentStream = $FileStream
$FileCreationInfo.URL = $SourceFileName
$FileUploaded = $Library.RootFolder.Files.Add($FileCreationInfo)
  
#powershell upload single file to sharepoint online
$Context.Load($FileUploaded)
$Context.ExecuteQuery()
 
#Close file stream
$FileStream.Close()
  
write-host "File has been uploaded!"

#Read more: https://www.sharepointdiary.com/2016/06/upload-files-to-sharepoint-online-using-powershell.html#ixzz6oldYfUeV
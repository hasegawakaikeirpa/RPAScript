#Nugetからダウンロードするスクリプト

try
{
    # パッケージプロバイダにNugetを追加
    Install-PackageProvider -Name Nuget

    # Nugetからパッケージ名を検索して、インストール実行
    Find-Package -Name Microsoft.SharePointOnline.CSOM -Source https://www.nuget.org/api/v2 -RequiredVersion 16.1.21012.12000 | Install-Package

    # パッケージのインストール確認
    Get-Package -ProviderName Nuget
}

catch [Exception]
{
    Write-Host $_.Exception.Message
}
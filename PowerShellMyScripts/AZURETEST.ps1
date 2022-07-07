$username = "hasegawarpa@hasegawakaikeirpa.onmicrosoft.com"
$password = "HaseK5121"
$AzCred = Get-Credential -UserName "42827d8c-7a42-40b2-b75a-02ba37ee1f83"
az login --service-principal -u $AzCred.UserName -p $AzCred.GetNetworkCredential().Password --tenant "f8cd21a0-3f1e-4378-ab3a-5d366d1a0d8f"
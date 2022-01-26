#az login

az account list

#az ad sp create-for-rbac --name ServicePrincipalName

#az login --service-principal --username  "appId": --password "password":  --tenant "tenant": 

az login --service-principal --username 64ecb8a2-ecc6-4c61-96e3-9a982982e820 --password QV8at_6a5zQ.4-Z8eAmCk3xD9FlrnlRkE5 --tenant f8cd21a0-3f1e-4378-ab3a-5d366d1a0d8f

az group create --name sp-sample --location eastus

az network vnet create -n sp-vnet -g sp-sample
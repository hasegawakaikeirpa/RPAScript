$Printers=Get-WmiObject Win32_Printer
$Printer=$Printers | Where-Object Name -eq "Microsoft Print to PDF"
# Powershell v2.0
# $Printer=$Printers | Where-Object {$_.Name -eq "Canon Generic Plus LIPSLX"}
$Printer.SetDefaultPrinter()
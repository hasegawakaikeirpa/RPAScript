import subprocess
mydirPath= "C:\pathTo\SomeStuff\\"
name= subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",  "Get-ChildItem "+ mydirPath +" -Force -Recurse | select @{Name=\"Owner\";Expression={(Get-ACL $_.Fullname).Owner}}"])
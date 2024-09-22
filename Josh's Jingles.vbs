Dim WshShell, strCurDir
Set WshShell = CreateObject("WScript.Shell") 
strCurDir = WshShell.CurrentDirectory & "\dpdc\start.bat"

WshShell.Run chr(34) & strCurDir & Chr(34), 0
Set WshShell = Nothing
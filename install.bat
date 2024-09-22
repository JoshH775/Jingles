@echo off
set origin=%cd%
echo %origin%
set desktop=%userprofile\desktop%
cd "%userprofile%\Desktop"
py -m pip --version
py -m pip install --upgrade pip
pip install pysimplegui
pip install pygame
pip install tinytag
pip install openpyxl
pip install mutagen
pip install validators
pip install moviepy
pip install pytube
pip install eyed3

set vbs=%origin%\Josh's Jingles.vbs
set batdir=%vbs%
set iconpath=%origin%\dpdc\images\icon.ico
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"
echo %origin%
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%origin%\Josh's Jingles.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%batdir%" >> %SCRIPT%
echo oLink.WorkingDirectory = "%origin%" >> %SCRIPT%
echo oLink.IconLocation = "%iconpath%" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%
del %SCRIPT%

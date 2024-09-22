@echo off
echo %cd%
set newdir=%cd%\dpdc

set startpy=\Window.py
set startpaths=%newdir%%startpy%



cd %userprofile%\desktop

python "%startpaths%" --user
pause


@echo off
:push
git pull
git add .
git status
set /p commitmsg=请输入提交信息：
git commit -m "commitmsg%"
git push -u origin master
git push -u coding master
goto push
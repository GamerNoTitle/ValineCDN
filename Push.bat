@echo off
:push
git pull
git add .
git status
set /p commitmsg=�������ύ��Ϣ��
git commit -m "commitmsg%"
git push -u origin master
git push -u coding master
goto push
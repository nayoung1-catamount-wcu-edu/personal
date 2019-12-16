git config --global user.name "nathayoung"

cd Land
start land.bat
cd..

cd Labor
start labor.bat
cd..

cd Earnings
start earnings.bat
cd..

cd Demographics
start Demographics.bat
cd..

pause
git commit -a -m "updating .bat files"
git status

pause
git push

git status
pause
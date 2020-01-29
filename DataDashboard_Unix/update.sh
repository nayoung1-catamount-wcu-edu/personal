echo Checking Installs
easy_install pip >nul
pip install jupyter --upgrade >nul
pip install jupyter lab --upgrade >nul
pip install pandas --upgrade >nul
pip install tensorflow --upgrade >nul
pip install Requests --upgrade >nul
pip install watermark --upgrade >nul
pip install xlrd --upgrade >nul
pip install pyodbc --upgrade >nul
pip install sqlalchemy --upgrade >nul
pip install numpy --upgrade >nul
echo Check complete!

echo Updating Land...
cd Land
bash land.sh
cd ..
echo Update complete!

echo Updating Demographics...
cd Demographics
bash demographics.sh
cd ..
echo Update complete!

echo Updating Labor...
cd Labor
bash labor.sh
cd ..
echo Update complete!

echo Update Earnings...
cd Earnings
bash earnings.sh
cd ..
echo Update complete!

sleep 5

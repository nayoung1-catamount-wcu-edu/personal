echo Checking Installs
Rem easy_install pip
Rem pip install jupyter --upgrade
Rem pip install jupyter lab --upgrade
Rem pip install pandas --upgrade
Rem pip install tensorflow --upgrade
Rem pip install Requests --upgrade
Rem pip install watermark --upgrade
Rem pip install xlrd --upgrade
Rem pip install pyodbc --upgrade
Rem pip install sqlalchemy --upgrade
Rem pip install numpy --upgrade
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

REM easy_install pip --upgrade
REM pip install jupyter --upgrade
REM pip install jupyter lab --upgrade
REM pip install pandas --upgrade
REM pip install tensorflow --upgrade
REM pip install Requests --upgrade
REM pip install watermark --upgrade
REM pip install xlrd --upgrade
REM pip install pyodbc --upgrade
REM pip install sqlalchemy --upgrade
REM pip install numpy --upgrade

git config --global user.name 'nathayoung'

cd Land
bash land.sh
cd ..

cd Demographics
bash demographics.sh
cd ..

cd Labor
bash labor.sh
cd ..

cd Earnings
bash earnings.sh
cd ..

sleep 5

cd Scripts

python -W ignore County_MedianListingPrice_AllHomes.py
python -W ignore County_MedianListingPricePerSqft_AllHomes.py
python -W ignore County_MedianValuePerSqft_AllHomes.py
python -W ignore County_Zhvi_AllHomes.py
python -W ignore GeoFRED_All_Transactions_House_Price_Index.py
python -W ignore GeoFRED_Homeownership_Rate_by_County.py
python -W ignore GeoFRED_New_Private_Housing_Structures.py

cd ..

cd Updates
git status

git commit -a -m "Land Update" date +"%m-%d-%Y"
git status

git push

cd ..



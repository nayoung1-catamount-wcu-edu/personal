git fetch
git pull

cd COVID\Data\covid-19-data

git fetch
git pull

cd..
cd..
cd..

"C:\Program Files\R\R-4.0.5\bin\R.exe" -e rsconnect::deployApp('C:/Users/natha/OneDrive/Desktop/GitHub/Personal/R/Shiny/COVID')

git add *
git commit -a -m "Updating COVID data for R Shiny App - %date%"

git push
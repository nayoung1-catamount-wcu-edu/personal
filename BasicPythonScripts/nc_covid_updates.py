import pandas as pd

files = 'C:/Users/natha/Downloads/NCDHHS_COVID-19_DataDownload.twbx'

pd.to_(files)





""" # Daily Metrics
dm = pd.read_csv('https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407877&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(dm.head())

# County Cases and Deaths
county_cases_and_deaths = pd.read_csv(
    'https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407878&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(county_cases_and_deaths.head())

# Zip Code Cases and Deaths
zip_cases_and_deaths = pd.read_csv(
    'https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407879&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(zip_cases_and_deaths.head())

# Demographics
race = pd.read_csv('https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407880&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(race.head())

ethnicity = pd.read_csv(
    'https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407881&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(ethnicity.head())

age = pd.read_csv('https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407882&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(age.head())

gender = pd.read_csv('https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407883&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(gender.head())

# Hospital Beds
hospital_beds = pd.read_csv(
    'https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407884&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(hospital_beds.head())

# Ventilators
ventilators = pd.read_csv(
    'https://public.tableau.com/vizql/w/NCDHHS_COVID-19_DataDownload/v/DailyMetrics/tempfile/sessions/75B3302F3E5C44078C0B73920A0078B4-0:0/?key=1856407885&keepfile=yes&attachment=yes', encoding='utf-16', sep='\t')

print(ventilators.head())
 """
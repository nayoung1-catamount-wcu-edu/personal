#!/usr/bin/env Python3.7

import pandas as pd
import time

df_mlp = pd.read_excel('./Data/County_MedianListingPrice_AllHomes.xlsx')
filter1 = df_mlp['State'] == "NC"
df_mlp_nc = df_mlp[filter1]
df_mlp_nc['MunicipalCodeFIPS'] = df_mlp_nc['MunicipalCodeFIPS'].astype(str)
df_mlp_nc['MunicipalCodeFIPS'] = df_mlp_nc['MunicipalCodeFIPS'].str.zfill(3)
df_mlp_nc.to_csv('./Data/STG_ZLLW_County_MedianListingPrice_AllHomes.txt')

time.sleep(5)

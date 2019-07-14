#!/usr/bin/env python3.7

hourly_pay = float(input('Enter hourly pay: '))
hours_worked = float(input('Enter hours worked: '))
day_pay = hourly_pay * hours_worked

total_sales = float(input('Enter sales: '))
commission = float(input('Enter commission: '))
day_sales = total_sales * commission

if day_pay > day_sales:
 print('Today you earned hourly pay equal to:',day_pay)
else:
 print('Today you earned commission equal to:',day_sales)
#!/usr/bin/env python3.7

## Hourly Wage ##
hourly_pay = float(input('Enter hourly pay: '))
hours_worked = float(input('Enter hours worked: '))
day_pay = hourly_pay * hours_worked

## Commission ##
total_sales = float(input('Enter sales: '))
commission = float(input('Enter commission: '))
day_sales = total_sales * commission


## Income ##
if day_pay > day_sales:
 print('Today you earned hourly pay equal to:',day_pay)
else:
 print('Today you earned commission equal to:',day_sales)
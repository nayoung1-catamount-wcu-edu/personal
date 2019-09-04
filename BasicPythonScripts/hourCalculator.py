time_limit = 25

ra = 17

print('Hours for RA:',ra)

tutoring = float(input('Enter hours for tutoring: '))

catTran = float(input('Enter hours for CatTran: '))

dataDashboard = float(input('Enter hours for Data Dashboard: '))

time_this_week = ra + tutoring + catTran + dataDashboard

print(time_this_week)

if time_this_week > time_limit:
    print('You worked too much this week!')
elif time_this_week == time_limit:
    print('Max score! Well done!')
else:
    print('You have too much free time this week!')

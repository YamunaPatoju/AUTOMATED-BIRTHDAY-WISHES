import datetime as dt

now = dt.datetime.now()
year = now.year
day = now.day
month = now.month
week_day = now.weekday()
print(week_day)
#print(f"this is {year} year and today day is {day}")

date_of_birth = dt.datetime(year= 2006 , month= 12 , day=2 , hour=9 , minute=30)
print(date_of_birth)
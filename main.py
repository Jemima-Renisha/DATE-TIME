from datetime import date,time,datetime

today = date.today()
now = datetime.now()

print("Today's date is",today)
print("current date and Time is",now)

print("date components:")
print(today.year)
print(today.month)
print(today.day)
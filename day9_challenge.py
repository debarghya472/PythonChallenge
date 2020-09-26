import datetime

current = datetime.datetime.now()

print('Todays date is',current.day)
print('Month',current.month)
print('Year is',current.year)
print('Today is',current.strftime("%A"))


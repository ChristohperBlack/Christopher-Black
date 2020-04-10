# today date
from datetime import datetime, timedelta

today = datetime.now()

print(today)

one_day = timedelta(days=1)
yesterday = today - one_day

print(yesterday)

a_week = input('Enter a date (dd/mm/yyyy): ')

a_week = datetime.strptime(a_week, '%d/%m/%Y')

one_week = timedelta(weeks=1)
later_week = a_week + one_week

print(later_week)

from datetime import date, timedelta

# Retrieve the current date using datetime.date.today()
today = date.today()

# Compute yesterday's date by subtracting 1 day from today's date using timedelta(days=1)
yesterday = today - timedelta(days=1)

# Compute tomorrow's date by adding 1 day to today's date using timedelta(days=1)
tomorrow = today + timedelta(days=1) 

# Output yesterday's date
print('Yesterday : ', yesterday)

# Output today's date
print('Today : ', today)

# Output tomorrow's date
print('Tomorrow : ', tomorrow)
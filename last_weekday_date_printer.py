# Process: Import the date class from the datetime module
from datetime import date
# Process: Import the timedelta class from the datetime module
from datetime import timedelta

# Retrieve the current date and assign it to the variable 'today'
today = date.today()

weekday = 1

# compute the offset needed to go back to the most recent weekday
# Process: This is done by finding the difference between the current weekday and target weekday, and taking modulo 7
offset = (today.weekday() - weekday) % 7

# compute the date of the most recent weekday by subtracting the offset from the current date
last_weekday = today - timedelta(days=offset)

# Output the date of the most recent weekday
print(last_weekday) 
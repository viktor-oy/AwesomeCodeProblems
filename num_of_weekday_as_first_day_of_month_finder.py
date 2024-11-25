# Process: Import the datetime class from the datetime module
from datetime import datetime

# Process: Initialize a counter to occurrence_count occurrences of Monday being the first day of the month
occurrence_count = 0

# Process: Define a range of months from 1 to 12
months = range(1, 13)

week_day = 0
start_year = 2015
end_year = 2019

for year in range(start_year, end_year + 1):
    # Process: Iterate over each month in the range
    for month in months:
        # verify whether the first day of the month (year, month, 1) falls on the weekday
        if datetime(year, month, 1).weekday() == week_day:
            # Process: If the first day of the month is a Monday, increment the counter
            occurrence_count += 1

# Output the total occurrence_count of occurrences where Monday is the first day of the month
print(occurrence_count)
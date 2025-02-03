# Process: Import the date class and the timedelta class from the datetime module
from datetime import date, timedelta

# Process: Define a function named all_sundays that takes a year as input
def all_sundays(year):
    # Process: Set dt to January 1st of the given year
    dt = date(year, 1, 1)
    # Process: Move dt to the first Sunday of the given year
    dt += timedelta(days=6 - dt.weekday())  
    # Process: Iterate through all Sundays of the given year
    while dt.year == year:
        # Process: Yield the current date (dt) as a result
        yield dt
        # Process: Move to the next Sunday by adding 7 days
        dt += timedelta(days=7)

year = int(input('Enter the year:'))

# Process: Iterate through all Sundays of the year using the all_sundays function
for s in all_sundays(year):
    # Output each Sunday
    print(s)
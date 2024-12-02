# Process: Import the datetime module
import datetime

num_of_dates = 12

# Process: Define a function named every_20_days that takes a date object (date) as input
def every_n_days(interval,date):
    # Output the starting date
    print('Starting Date: {d}'.format(d=date))
    # Output a message indicating the next 12 days
    print("Next %s days :" % num_of_dates )

    for _ in range(num_of_dates):
        # Include n days to the current date
        date = date + datetime.timedelta(days=interval)
        # Output the resulting date
        print('{d}'.format(d=date))

year = 2016
interval = 20

# Process: Define a date object representing the date
dt = datetime.date(year, 1, 1)

# Process: Call the every_20_days function with the specified date object
every_n_days(interval , dt)
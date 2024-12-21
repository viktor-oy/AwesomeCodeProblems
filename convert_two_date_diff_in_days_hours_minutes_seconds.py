# Process: Import the datetime and time classes from datetime module
from datetime import datetime, time

# Process: Define a function called date_diff_in_seconds which calculates the difference in seconds between two datetime objects
def date_diff_in_seconds(dt2, dt1):
    # compute the time difference between dt2 and dt1
    timedelta = dt2 - dt1
    # Yield the total time difference in seconds
    return timedelta.days * 24 * 3600 + timedelta.seconds

# Process: Define a function called dhms_from_seconds which converts seconds into days, hours, minutes, and seconds
def dhms_from_seconds(seconds):
    # Compute minutes and remaining seconds
    minutes, seconds = divmod(seconds, 60)
    # Compute hours and remaining minutes
    hours, minutes = divmod(minutes, 60)
    # Compute days and remaining hours
    days, hours = divmod(hours, 24)
    # Yield days, hours, minutes, and seconds
    return (days, hours, minutes, seconds)

# Process: Specified date: January 1, 2015, at 01:00:00
date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
# Process: Current date and time
date2 = datetime.now()

# Output the time difference in days, hours, minutes, and seconds between the current date and the specified date
print("\n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
# Output an empty line
print()
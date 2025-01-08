from datetime import datetime 

# Process: Define a function named is_third_tuesday that takes a date string (s) as input
def is_third_tuesday(s):
    # Transform the input date string to a datetime object using the specified format '%b %d, %Y'
    d = datetime.strptime(s, '%b %d, %Y')

    # verify whether the weekday of the date is Tuesday (1) and the day of the month is between 15 and 21
    # Process: This condition ensures that the date is the third Tuesday of the month
    return d.weekday() == 1 and 14 < d.day < 22

# Output the result of calling is_third_tuesday with different date strings
print(is_third_tuesday('Jun 23, 2015'))  # False
print(is_third_tuesday('Jun 16, 2015'))  # True
print(is_third_tuesday('Jul 21, 2015'))  # False
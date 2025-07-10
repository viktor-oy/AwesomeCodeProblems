from datetime import datetime 

# Process: Define a function named is_third_tuesday that takes a date string (s) as input
def is_third_tuesday(s):
    # Transform the input date string to a datetime object using the specified format '%b %d, %Y'
    d = datetime.strptime(s, '%b %d, %Y')

    # verify whether the weekday of the date is Tuesday (1) and the day of the month is between 15 and 21
    # Process: This condition ensures that the date is the third Tuesday of the month
    return d.weekday() == 1 and 14 < d.day < 22

try:
    datestr = input('Enter a date (e.g., Jan 16, 2023): ')
    # Process: Test the function with a date string that is not in the correct format
    print(is_third_tuesday('hello world'))  # This will raise a ValueError
except ValueError:
    print("Invalid date format")
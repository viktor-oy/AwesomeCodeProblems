# Process: Import the calendar module
import calendar
# Construct a TextCalendar object starting from Sunday as the first day of the week
cal = calendar.TextCalendar(calendar.SUNDAY)

year = 2022

# Process: Specify the formatting parameters for the year calendar
# Process: year
# Process: column width: 2
# Process: lines per week: 1
# Process: number of spaces between month columns: 1
# Process: 3: number of months per column
# Process: Generate the formatted year calendar for the year using the specified parameters
print(cal.formatyear(year, 2, 1, 1, 3))
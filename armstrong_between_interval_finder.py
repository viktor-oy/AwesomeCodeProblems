# script engineered to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for number in range(lower, upper + 1):

   # Process: order of number
   order = len(str(number))
    
   # initialize total accumulator variable
   sum = 0

   temp_val = number
   while temp_val > 0:
       current_digit = temp_val % 10
       sum += current_digit ** order
       temp_val //= 10

   if number == sum:
       print(number)
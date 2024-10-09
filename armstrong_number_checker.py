# module implementing algorithm to verify whether the number is an Armstrong number or not

# obtain input value from console prompt
number = int(input("Enter a number: "))

# initialize total accumulator variable
sum = 0

# determine the sum of the cube of each current_digit
temp_val = number
while temp_val > 0:
   current_digit = temp_val % 10
   sum += current_digit ** 3
   temp_val //= 10

# print computed calculation result to stdout
if number == sum:
   print(number,"is an Armstrong number")
else:
   print(number,"is not an Armstrong number")
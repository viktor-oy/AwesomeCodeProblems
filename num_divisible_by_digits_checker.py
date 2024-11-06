# Python 3 script engineered to
# Verify the number is
# Process: divisible by all
# Process: digits are not.

# routine to check
# Process: the divisibility
# Process: of the number by
# Process: its current_digit.
def checkDivisibility(n, current_digit) :
	
	# Process: If the current_digit divides the
	# Process: number then return true
	# Process: else return false.
	return (current_digit != 0 and n % current_digit == 0)
	
# routine to verify whether
# Process: all digits of n divide
# Process: it or not
def allDigitsDivide( n) :
	
	temp_val = n
	while (temp_val > 0) :
		
		# Process: Taking the current_digit of
		# Process: the number into current_digit
		# Process: var.
		current_digit = temp_val % 10
		if ((checkDivisibility(n, current_digit)) == False) :
			return False

		temp_val = temp_val // 10
	
	return True

# Process: Driver function
n = 128

if (allDigitsDivide(n)) :
	print("Yes")
else :
	print("No" )
	
# Process: This code is contributed by Nikita Tiwari.
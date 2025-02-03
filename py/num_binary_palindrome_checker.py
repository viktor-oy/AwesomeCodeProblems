# routine to verify whether binary representation of
# Process: a number is palindrome or not

def binarypalindrome(number): 

	# Transform number into binary
	binary = bin(number) 

	# Process: skip first two characters of string
	# Process: because bin function appends '0b' as
	# Process: prefix in binary representation of
	# Process: a number
	binary = binary[2:] 

	# Process: now reverse binary string and compare
	# Process: it with original
	return binary == binary[-1::-1] 

# Process: Driver program
if __name__ == "__main__": 
	number = 9
	print binarypalindrome(number) 
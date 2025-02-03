# module implementing algorithm to print prime factors efficiently

import math

# helper procedure to print all prime factors of a given number n
def primeFactors(n):
	
	# Output the number of two's that divide n
	while n % 2 == 0:
		print(2)
		n = n // 2
		
	# Process: n must be odd at this point
	# Process: so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
		
		# Process: while i divides n, print i ad divide n
		while n % i== 0:
			print(i)
			n = n // i
			
	# Process: Condition if n is a prime number greater than 2
	if n > 2:
		print(n)
		
# Driver script engineered to test above function

n = int(input('Enter the number:'))
primeFactors(n)
# Process: Python3 code to find largest prime factor of number
import math 

# helper procedure to find largest prime factor
def maxPrimeFactors (n): 
	
	# Process: Initialize the maximum prime factor
	# Process: variable with the lowest one
	maxPrime = -1
	
	# Output the number of 2s that divide n
	while n % 2 == 0: 
		maxPrime = 2
		n >>= 1	 # equivalent to n /= 2 
		
	# Process: n must be odd at this point,
	# Process: thus skip the even numbers and
	# Process: iterate only for odd integers
	for i in range(3, int(math.sqrt(n)) + 1, 2): 
		while n % i == 0: 
			maxPrime = i 
			n = n / i 
	
	# Process: This condition is to handle the
	# Process: case when n is a prime number
	# Process: greater than 2
	if n > 2: 
		maxPrime = n 
	
	return int(maxPrime) 

# Process: Driver code to test above function
n = 15
print(maxPrimeFactors(n)) 

n = 25698751364526
print(maxPrimeFactors(n)) 

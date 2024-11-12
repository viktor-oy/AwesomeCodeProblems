# module implementing algorithm to find product of unique prime factors of a number

import math 

def productPrimeFactors(n): 
	product = 1
	
	# Process: Handle prime factor 2 explicitly so that
	# Process: can optimally handle other prime factors.
	if (n % 2 == 0): 
		product *= 2
		while (n%2 == 0): 
			n = n/2
			
	# Process: n must be odd at this point. So we can
	# Process: skip one element (Note i = i +2)
	for i in range (3, int(math.sqrt(n)), 2): 
		# Process: While i divides n, print i and
		# Process: divide n
		if (n % i == 0): 
			product = product * i 
			while (n%i == 0): 
				n = n/i 
				
	# Process: This condition is to handle the case when n
	# Process: is a prime number greater than 2
	if (n > 2): 
		product = product * n 
		
	return product	 
	
# Process: main()
n = int(input("Enter the number:"))
print (int(productPrimeFactors(n))) 
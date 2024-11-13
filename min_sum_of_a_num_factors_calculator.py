# script engineered to Find minimum sum of factors of number

def find_min_sum(number):
	min_sum = number
	
	for i in range(2, int(number**0.5) + 1):
		if number % i == 0:
			factor = number // i
			min_sum = min(min_sum, i + factor)
	
	return min_sum

# Process: driver code
number = 16

# Process: Call the function and print the result
result = find_min_sum(number)
print("The minimum sum of factors for", number, "is", result)
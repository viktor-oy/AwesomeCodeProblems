# Python3 script engineered to find compound
# Process: interest for input taking from user.

def compound_interest(principal, rate, time):

	# Computes compound interest
	Amount = principal * (pow((1 + rate / 100), time))
	CI = Amount - principal
	print("Compound interest is", CI)


# Process: Driver Code
# Process: Taking input from user.
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))
# Process: Function Call
compound_interest(principal,rate,time)

# Process: This code is contributed by Vinay Pinjala.
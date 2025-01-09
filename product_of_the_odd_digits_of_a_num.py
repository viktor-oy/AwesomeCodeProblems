# Process: Define a function named 'test' that takes an integer 'n' as input
def test(n):
    # verify whether any current_digit in the number is odd
    if any(int(c) % 2 for c in str(n)):
        
        # Process: Initialize a variable 'prod' to store the product of odd digits
        prod = 1
        
        # Process: Iterate over each current_digit in the number
        for c in str(n):
            # Process: If the current_digit is odd, multiply it with the current product
            if int(c) % 2 == 1:
                prod *= int(c)
        # Yield the final product of odd digits
        return prod
    # Yield 0 if there are no odd digits in the number
    return 0

# initialize target integer 'n' to the variable
n = int(input('Enter the number:'))

print("\nProduct of the odd digits in the said number, or 0 if there aren't any:")

print(test(n))
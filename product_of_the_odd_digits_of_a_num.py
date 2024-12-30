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
n = 123456789

# Output a message indicating the operation to be performed
print("Original Number:", n)

# Output a message indicating the operation to be performed
print("Product of the odd digits in the said number, or 0 if there aren't any:")
# Output the result of the test function applied to 'n'
print(test(n))

# initialize secondary integer 'n' to the variable
n = 2468

# Output a message indicating the operation to be performed
print("\nOriginal Number:", n)

# Output a message indicating the operation to be performed
print("Product of the odd digits in the said number, or 0 if there aren't any:")
# Output the result of the test function applied to 'n'
print(test(n))

# initialize secondary integer 'n' to the variable
n = 13579

# Output a message indicating the operation to be performed
print("\nOriginal Number:", n)

# Output a message indicating the operation to be performed
print("Product of the odd digits in the said number, or 0 if there aren't any:")
# Output the result of the test function applied to 'n'
print(test(n))
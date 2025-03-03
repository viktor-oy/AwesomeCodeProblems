# Process: Define a function named 'test' that takes a list of numbers 'nums' and an integer 'k' as input
def test(nums, k):
    # Process: Initialize a variable 's' to store the sum of numbers meeting the specified conditions
    s = 0
    # Process: Iterate through the first 'k' elements in 'nums'
    for i in range(len(nums))[:k]:
        # verify whether the absolute value of the current number has more than 2 digits
        if len(str(abs(nums[i]))) > 2:
            # Include the current number to the sum 's'
            s = s + nums[i]
    # Yield the final sum 's'
    return s

# initialize target list of numbers 'nums' to the variable
nums = [4, 5, 17, 9, 14, 108, -9, 12, 76]

# Output a message indicating the operation to be performed
print("Original list:", nums)

# initialize target value 'K' to the variable
K = 4

# Output a message indicating the value of 'K'
print("Value of K:", K)

# Output a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Output the result of the test function applied to 'nums' and 'K'
print(test(nums, K))

# initialize secondary value 'K' to the variable
K = 6

# Output a message indicating the value of 'K'
print("\nOriginal list:", nums)
print("Value of K:", K)

# Output a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Output the result of the test function applied to 'nums' and 'K'
print(test(nums, K))

# initialize secondary list of numbers 'nums' to the variable
nums = [114, 215, -117, 119, 14, 108, -9, 12, 76]

# Output a message indicating the operation to be performed
print("\nOriginal list:", nums)

# initialize secondary value 'K' to the variable
K = 5

# Output a message indicating the value of 'K'
print("Value of K:", K)

# Output a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Output the result of the test function applied to 'nums' and 'K'
print(test(nums, K))

# Output an additional message indicating the original list
print("\nOriginal list:", nums)

# initialize secondary value 'K' to the variable
K = 1

# Output a message indicating the value of 'K'
print("Value of K:", K)

# Output a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Output the result of the test function applied to 'nums' and 'K'
print(test(nums, K))
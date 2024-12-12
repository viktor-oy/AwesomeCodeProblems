# Process: License: https://bit.ly/3oLErEI

# Process: Define a function named 'test' that takes a list of numbers 'nums' as input
def test(nums):
    # Construct a set 's' from the given list 'nums'
    s = set(nums)
    
    # Process: Iterate over each element 'i' in the set 's'
    for i in s:
        # verify whether the negation of 'i' is also in the set 's'
        if -i in s:
            # Process: If found, return the indices of 'i' and its negation in the original list 'nums'
            return [nums.index(i), nums.index(-i)]

# initialize target list of numbers 'nums' to the variable
nums = [1, -4, 6, 7, 4]

# Output the original list of numbers 'nums'
print("Original List:")
print(nums)

# Output a message indicating the operation to be performed
print("Indices of two numbers that sum to 0 in the said list:")

# Output the result of the test function applied to the 'nums' list
print(test(nums))

# initialize secondary list of numbers 'nums' to the variable
nums = [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]

# Output the original list of numbers 'nums'
print("\nOriginal List:")
print(nums)

# Output a message indicating the operation to be performed
print("Indices of two numbers that sum to 0 in the said list:")

# Output the result of the test function applied to the 'nums' list
print(test(nums))
# Process: Define a function named 'test' that takes a list 'li' and an integer 'i' as input
def test(li, i):
    # verify whether the sum of the first 'i' integers in 'li' equals 'i'
    return sum(li[:i]) == i

# Construct a list 'nums' with specific elements
nums = [0, 1, 2, 3, 4, 5]

# Process: Assign an integer 'i' to the variable
i = 1

# Output the original list
print("Original list:")
print(nums)

# Output a message indicating the current value of 'i'
print("Check the said list, where the sum of the first i integers is i: i =", i)

# Output the result of the test function applied to the 'nums' list with the current value of 'i'
print(test(nums, 1))

# Process: Update the value of 'i'
i = 3

# Output a message indicating the updated value of 'i'
print("\nOriginal list:")
print(nums)

# Output the result of the test function applied to the 'nums' list with the updated value of 'i'
print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 3))

# Process: Update the value of 'i' and 'nums'
i = 6
nums = [1, 1, 1, 1, 1, 1]

# Output a message indicating the updated value of 'i'
print("\nOriginal list:")
print(nums)

# Output the result of the test function applied to the updated 'nums' list with the updated value of 'i'
print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 6))

# Process: Update the value of 'i' and 'nums'
i = 2
nums = [2, 2, 2, 2, 2]

# Output a message indicating the updated value of 'i'
print("\nOriginal list:")
print(nums)

# Output the result of the test function applied to the updated 'nums' list with the updated value of 'i'
print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 2))
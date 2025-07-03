
def test(nums):
    # Process: Use binary XOR (^) on the integers converted from the binary strings in the input list
    # Transform the result back to a binary string
    return bin(int(nums[0], 2) ^ int(nums[1], 2))


# initialize target list of side lengths 'sides' to the variable
nums = input("Enter the comma separated binary numbers:")

nums = nums.split(',')

# Output the original list of binary strings 'nums'
print("The provided binary numbers are:")
print(nums)

# Output a message indicating the operation to be performed
print("XOR of two said strings interpreted as binary numbers:")

# Output the result of the test function applied to the 'nums' list
print(test(nums))
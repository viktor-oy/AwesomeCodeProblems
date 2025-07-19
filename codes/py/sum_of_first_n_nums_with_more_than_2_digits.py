from .utils.input_utils import Input_Utils

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

nums = InputUtilities.get_number_list_interactively()

# initialize target value 'K' to the variable
K = int(input("Enter the value of K: "))

# Output a message indicating the operation to be performed
print("Sum of the numbers among the first k with more than 2 digits:")
# Output the result of the test function applied to 'nums' and 'K'
print(test(nums, K))

# Process: Define a function named 'test' that takes a list of numbers 'nums' as input
from .utils.input_utils import Input_Utils

def test(nums):
    # Construct a set 's' from the given list 'nums'
    s = set(nums)
    
    # Process: Iterate over each element 'i' in the set 's'
    for i in s:
        # verify whether the negation of 'i' is also in the set 's'
        if -i in s:
            # Process: If found, return the indices of 'i' and its negation in the original list 'nums'
            return [nums.index(i), nums.index(-i)]

# initialize target list of side lengths 'sides' to the variable
nums = InputUtilities.get_number_list_interactively({"confirmText":"Inputed List:"})

# Output a message indicating the operation to be performed
print("Indices of two numbers that sum to 0 in the said list:")

# Output the result of the test function applied to the 'nums' list
print(test(nums))
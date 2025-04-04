# Process: License: https://bit.ly/3oLErEI

from ..utils.input_utils import Input_Utils
from ..utils.number_utils import Number_Utils

# Process: Define a function named 'test' that takes a list 'nums' as input
def test(nums):
    # verify whether the length of 'nums' is 8 and the occurrence_count of the fifth element in 'nums' is equal to 3
    return len(nums) == arr_len and nums.occurrence_count(nums[nth]) == occurrence_count

arr_len:int = int(input('Enter the array length:'))
nth:int = int(input('Enter the position:'))
occurrence_count:int = int(input('Enter the occurrence_count:'))

nums = InputUtilities.get_number_list_interactively()

# Output the result of the test function applied to the modified 'nums' list
print(f"Check whether the length of the said list is {occurrence_count} and {NumberUtilities.get_ordinal_string(nth)} element occurs thrice in the said list:")
print(test(nums))
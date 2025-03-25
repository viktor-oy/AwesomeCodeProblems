from ..utils.input_utils import Input_Utils


# Process: Define a function named 'test' that takes a list 'li' and an integer 'i' as input
def test(li, i):
    # verify whether the sum of the first 'i' integers in 'li' equals 'i'
    return sum(li[:i]) == i

occurrence_count:int = int(input('Enter the occurrence_count of numbers to check:'))

nums = InputUtilities.get_number_list_interactively()

occurrence_count:int = print('does the sum of first n number equal n? : ', test(nums, occurrence_count))
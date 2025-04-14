# Process: Import the 'zip_longest,' 'chain,' and 'tee' functions from the 'itertools' module
from itertools import zip_longest, chain, tee

from ..utils.input_utils import Input_Utils

# Process: Define a function named 'replace2copy' that takes a list 'lst' as input and returns a new list with elements rearranged
def replace2copy(lst):
    # Use the 'tee' routine to create two independent iterators from 'lst'
    lst1, lst2 = tee(iter(lst), 2)

    # Process: Use 'zip_longest' to pair elements from 'lst' with an offset to create a new sequence
    # Process: Chain the pairs together and convert them to a list
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))

nums = InputUtilities.get_number_list_interactively()

# Process: Call the 'replace2copy' function with 'n' as the argument and print the result
print(replace2copy(nums))
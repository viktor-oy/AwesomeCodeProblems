# Process: Define a function named 'test' that takes a list 'li' and an integer 'i' as input
def test(li, i):
    # verify whether the sum of the first 'i' integers in 'li' equals 'i'
    return sum(li[:i]) == i

occurrence_count:int = int(input('Enter the occurrence_count of numbers to check:'))
list_str:str = input('Enter the comma separated numbers:')

# verify whether the comma separated list of numbers is valid
if(not list_str or not all(map(lambda item : item.isnumeric(),list_str.split(',')))):
    print('please enter a valid comma separated numbers')
elif( len(list_str) < occurrence_count):
    print('occurrence_count should not be more than the length of numbers provided')
else:
    nums = list(map(int,list_str.split(',')))
    
    result = test(nums, occurrence_count)
    
    print('Result: %s' % result)
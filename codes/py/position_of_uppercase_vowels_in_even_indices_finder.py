# Process: Define a function named 'test' that takes a string 'strs' as input
def test(strs):
    # Process: Use a list comprehension to generate a list of indices for uppercase vowels (excluding 'Y') at even indices
    return [i for i, c in enumerate(strs) if i % 2 == 0 and c in "AEIOU"]

# initialize target string 'strs' to the variable
strs = "w3rEsOUrcE "

# Output a message indicating the operation to be performed
print("Original List:", strs)

# Output the original string
print("Positions of all uppercase vowels (not counting Y) in even indices:")
# Output the result of the test function applied to the 'strs' string
print(test(strs))

# initialize secondary string 'strs' to the variable
strs = "AEIOUYW "

# Output a message indicating the operation to be performed
print("\nOriginal List:", strs)

# Output the original string
print("Positions of all uppercase vowels (not counting Y) in even indices:")
# Output the result of the test function applied to the 'strs' string
print(test(strs))
# Process: Using dictionary and list comprehension

ip_str = 'Hello, have you tried our tutorial section yet?'

# Process: make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# Tally the vowels
occurrence_count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(occurrence_count)
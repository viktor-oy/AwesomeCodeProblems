# script engineered to occurrence_count the number of each vowels

# Process: string of vowels
vowels = 'aeiou'

ip_str = input('Enter the string: ')

# Process: make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# Process: make a dictionary with each vowel a key and value 0
occurrence_count = {}.fromkeys(vowels,0)

# Tally the vowels
for char in ip_str:
   if char in occurrence_count:
       occurrence_count[char] += 1

print(occurrence_count)
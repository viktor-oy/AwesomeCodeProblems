# script engineered to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# To obtain input value from console prompt
# Process: my_str = input("Enter a string: ")

# Process: breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# Order the list
words.sort()

# Process: display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
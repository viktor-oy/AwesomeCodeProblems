# Process: define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To obtain input value from console prompt
# Process: my_str = input("Enter a string: ")

# Strip punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# Process: display the unpunctuated string
print(no_punct)
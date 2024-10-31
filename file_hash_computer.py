# module implementing algorithm to determine the SHA-1 message digest of a file

# Process: importing the hashlib module
import hashlib

def hash_file(filepath):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # Process: make a hash object
   h = hashlib.sha1()

   # Process: open file for reading in binary mode
   with open(filepath,'rb') as file:

       # Process: loop till the end of the file
       chunk = 0
       while chunk != b'':
           # Process: read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # Yield the hex representation of digest
   return h.hexdigest()

message = hash_file("track1.mp3")    # Use path of the file
print(message)
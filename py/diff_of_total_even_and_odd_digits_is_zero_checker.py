# script engineered to verify whether the difference between Sums of Odd and Even Digits is 0

def isDiff0(n):
    first = 0
    second = 0
    flag = True
    while(n > 0):
        current_digit = n % 10
        if(flag):
            first += current_digit
        else:
            second += current_digit
        if(flag):
            flag = False
        else:
            flag = True
        n = int(n/10)
    if(first-second == 0):
        return True
    return False
 
 
# Process: driver code
n = 1243
if(isDiff0(n)):
    print("Yes")
else:
    print("No")
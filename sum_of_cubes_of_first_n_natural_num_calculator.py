# Simple module implementing algorithm to find sum of series with cubes of first n natural numbers

# Process: Returns the sum of series
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i*i
        
    return sum


# Process: Driver Function
n = int(input("Enter the number:"))
print(sumOfSeries(n))
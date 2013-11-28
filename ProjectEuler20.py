__author__ = 'matt'
def getFactorial(n):
    product = 1
    for x in range (n,1,-1):
        product = product * x
    return product
val = getFactorial(100)
stringVal = str(val)
sum = 0
for y in stringVal:
    digit = int(y)
    sum += digit
print sum
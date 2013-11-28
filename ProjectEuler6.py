__author__ = 'matt'
squareSum = 0
sum = 0
for x in range(1,101):
    sum += x
    squareSum += (x**2)
print (sum**2 - squareSum)

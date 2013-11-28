__author__ = 'matt'
import math
def getDigitsOfNum(num):
    digits = []
    n = str(num)
    for y in n:
        digits.append(int(y))
    return digits
def sumFactorialDigits(n):
    sum = 0
    digits = getDigitsOfNum(n)
    for x in digits:
        num = math.factorial(x)
        sum += num
    return sum
def getSumFactNumbs():
    values = []
    for x in range(1,1000000):
        if(x == sumFactorialDigits(x)):
            values.append(x)
    return values
vals = getSumFactNumbs()
vals.remove(1)
vals.remove(2)
print vals
sum = 0
for x in vals:
    sum += x
print sum
__author__ = 'matt'
def getDigitsOfNum(num):
    digits = []
    n = str(num)
    for y in n:
        digits.append(int(y))
    return digits
def sumPowerNumberDigits(num, p):
    digits = getDigitsOfNum(num)
    sum = 0
    for x in digits:
        sum += (x**p)
    return sum
def getSumPowerNumbers(p):
    vals = []
    for x in range(2,1000000): #ignore 1
        if(x == sumPowerNumberDigits(x,p)):
            vals.append(x)
    return vals
vals =  getSumPowerNumbers(5)
sum = 0
for x in vals:
    sum += x
print sum

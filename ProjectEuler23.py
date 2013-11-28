__author__ = 'matt'
import itertools
def factors(n):
    val =  set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
    val.remove(n)
    return val
def sumFactors(n):
    sum = 0
    for x in factors(n):
        sum+=x
    return sum
def isAbudant(n):
    if(sumFactors(n) > n):
        return True
    return False
def getAbundantNumbers(topValue):
    vals = []
    for x in range(1,topValue):
        if isAbudant(x):
            vals.append(x)
    return vals
def comboOfAbundant(n, anumbers):
    if((n/2) + (n/2) == n and n/2 in anumbers):
        return True
    vals = list(itertools.combinations(anumbers, 2))
    for x in vals:
        if((x[0] + x[1]) == n):
            return True
        if n==24:
            print x[0]
            print x[1]
    return False


def getNotComboOfAbundant(topValue):
    vals = []
    anumbers = getAbundantNumbers(topValue)
    for x in range(1,topValue):
        if(not comboOfAbundant(x,anumbers)):
            vals.append(x)
    return vals
#28123
vals= getNotComboOfAbundant(5000)


sum = 0
for x in vals:
    sum += x
print sum

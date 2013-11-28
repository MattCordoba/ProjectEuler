__author__ = 'matt'
def getRecurringCycleLength(n):
    modifier = 10
    visited = []
    count = 0
    val = 1
    while(val != 0):
        val = modifier % n
        if val in visited:
            return count
        visited.append(val)
        modifier = 10*val
        count = count + 1
    return count
#gets all primes below a certain upperlimit
def get_primes(upperlimit):
    allNumbers = set(range(upperlimit, 1, -1))
    primes = []
    while allNumbers:
        num = allNumbers.pop()
        primes.append(num)
        allNumbers.difference_update(set(range(num*2, upperlimit+1, num)))
    return primes
#only need primes
list = get_primes(1000)
#ignore 2,3,5
list.pop(0)
list.pop(0)
list.pop(0)
topVal = 0
topX = 0
for x in list:
    val = getRecurringCycleLength(x)
    if(val > topVal):
        topVal = val
        topX = x
print topX


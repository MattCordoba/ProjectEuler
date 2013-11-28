__author__ = 'matt'
#gets all primes below a certain upperlimit
def get_primes(upperlimit):
    allNumbers = set(range(upperlimit, 1, -1))
    primes = []
    while allNumbers:
        num = allNumbers.pop()
        primes.append(num)
        allNumbers.difference_update(set(range(num*2, upperlimit+1, num)))
    return primes
vals = get_primes(2000000)
sum = 0
for x in vals:
    sum += x
print sum
__author__ = 'matt'
def factors(n):
    return set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
def sumFactors(vals):
    sum = 0
    for x in vals:
        sum+= x
    return sum
import time
start = time.time()
sum = 0
for x in range(1,10000):
    val = sumFactors(factors(x)) - x #d(a) x = a val= b
    secondVal = sumFactors(factors(val)) - val #d(b) = a
    if(secondVal == x and val != secondVal):
        sum+=val
        sum+=secondVal
print sum/2
end = time.time()
print end - start
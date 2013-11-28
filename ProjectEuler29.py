__author__ = 'matt'
import itertools
def generateSeq(low,high):
    vals = []
    nums = []
    for x in range(low, high +1):
        nums.append(x)
        vals.append(x**x)
    combos = list(itertools.combinations(nums,2))
    for y in combos:
        num1 = y[0]
        num2 = y[1]
        vals.append((num1**num2))
        vals.append((num2**num1))
    setVals = set(vals)
    vals = list(setVals)
    return vals
import time
start = time.time()
end = time.time()
vals = generateSeq(2,100)
print len(vals)
print "Process completed in " + str(end - start) + " s"
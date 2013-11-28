__author__ = 'matt'
import math
#Iteratarable fib sequence.... provides a much quicker and cleaner way
# to find fibonacci sequence
def fibIter():
    cur = 0
    prev = 1
    temp = 0
    while True:
        temp = cur
        cur = cur + prev
        prev = temp
        yield cur

def getDigitCount(n):
    return len(str(n))
for i,x in enumerate(fibIter()):
    digitCount = getDigitCount(x)
    if digitCount >= 1000:
        print i + 1 #found
        break


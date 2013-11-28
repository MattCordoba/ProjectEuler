__author__ = 'matt'
import itertools
vals = [0,1,2,3,4,5,6,7,8,9]
vals = list(itertools.permutations(vals))
vals.sort()
print vals[999999] # 1millionth val

__author__ = 'matt'
def ispalindrome(string1):
    string2 = string1[::-1]
    if string1 == string2:
        return True
    return False
def get_binary_val(n):
    return "{0:b}".format(n)
vals = []
for x in range(1,1000000):
    if not ispalindrome(str(x)):
        continue
    binaryStr = get_binary_val(x)
    if ispalindrome(binaryStr):
        vals.append(x)
sum = 0
for y in vals:
    sum+=y
print sum
872187
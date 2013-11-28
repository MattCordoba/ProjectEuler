__author__ = 'matt'
def ispalindrome(string1):
    string2 = string1[::-1]
    if string1 == string2:
        return True
    return False

maxproduct = 0
maxX = 0
maxY = 0
for x in range(1, 1000):
    for y in range(2, 1000):
        product = x*y
        if ispalindrome(str(product)):
            if product > maxproduct:
                maxX = x
                maxY =y
                maxproduct = product

print maxproduct
print maxX
print maxY
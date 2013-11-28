__author__ = 'matt'
for x in range(200000000, 300000000):
    allDivides = True
    for y in range(1,20):
        if x%y != 0:
            allDivides = False
            break
    if(allDivides):
        print x
        break


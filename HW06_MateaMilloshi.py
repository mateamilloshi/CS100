'''
Matea Milloshi CS100 
2021F Section 105 HW 06,
October 20, 2021
'''

#1a
def hasFinalLetter(strList, letters):
    result = []
    for item in strList:
        if item[-1] in letters:
            result.append(item)

    return result

#1b
strList = ['book','car','orange']
letters='re'
print(hasFinalLetter(strList,letters))

#empty list
strList = [['jacket', 'shoes', 'aeroplane']]
letters='lg'
print(hasFinalLetter(strList,letters))

strList = ['dog', 'train', 'bike']
letters='ge'
print(hasFinalLetter(strList,letters))

#2a
def isDivisible(maxInt, twoInts):
    dlist = []
    num1 = twoInts[0]
    num2 = twoInts[1]
    for i in range(1,maxInt):
        if i % num1 == 0 and i % num2 == 0:
            dlist.append(i)
    return dlist

#2b
maxInt=60
twoInts=[5,10]
print(isDivisible(maxInt,twoInts))

#empty list
maxInt=0
twoInts=[3,7]
print(isDivisible(maxInt,twoInts))

maxInt=40
twoInts=[2,8]
print(isDivisible(maxInt,twoInts))

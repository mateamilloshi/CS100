#Matea Milloshi
#CS 100 2021F Section 105
#HW05, October 3,2021

#1
months=['January','February','March','April','May','June',
        'July','August','September','October','November','December']
for i in months:
    if i[0]=='J':
        print(i)

#2
for i in range(0,100):
    if i%2==0 and i%5==0:
        print(i)

#3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for i in horton:
    if i in vowels:
        print(i)

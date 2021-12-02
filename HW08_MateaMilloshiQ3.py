'''
#Matea Milloshi
#CS 100 2021F Section 105
#HW08, November 2,2021
'''

#Problem 3
def enterNewPassword():
    while True:
        password=input("Please type a password btw 8-15 characters, including a digit: ")
        if (8<= len(password)<=15): 
            for i in password:
                if i.isdigit():
                    return password
            print(" ERROR!! your password is missing a digit ")
        else:
            print(" ERROR!! incorrect length of the password ")    

print(enterNewPassword()) 
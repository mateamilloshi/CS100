'''
#Matea Milloshi
#CS 100 2021F Section 105
#HW08, November 2,2021
'''
#Problem 2
def twoWordsV2(length, firstLetter):
    wordlength=input('Enter a '+ str(length)+ ' letter word please ')
    while len(wordlength)!= length:
        wordlength=input('Enter a '+ str(length)+ ' letter word please ')
    the_letter=input('Enter a word starting with letter '+firstLetter+' for second word please')  
    while the_letter[0].lower() != firstLetter.lower():
        the_letter=input('Enter a word starting with letter '+firstLetter+' for second word please')
    return [wordlength, the_letter]

print(twoWordsV2(5, 'm'))
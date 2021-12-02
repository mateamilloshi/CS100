'''
#Matea Milloshi
#CS 100 2021F Section 105
#HW08, November 2,2021
'''
#Problem 1
def twoWords(length,firstLetter):
  while True:
    wordLen=input('Enter a ' + str(length) + ' letter word please')
    if len(wordLen)==length:
      break
  while True:
    the_letter=input('Enter a word starting with letter '+firstLetter+' for second word please ')
     if (the_letter[0].lower()== firstLetter.lower()):
            break
    return[wordLen, the_letter]

print(twoWords(5, 'm'))


                                         
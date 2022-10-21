'''
Define a function inverse() that calculates the inversion of a string. 
For example the string "I am testing" should return the string "gnitset ma I"
'''

def inverse(string):
    newString = ''
    for i in range(len(string)):
        newString = string[i] + newString
    return newString

print("The inverse of 'I am testing' is: ", inverse('I am testing'))
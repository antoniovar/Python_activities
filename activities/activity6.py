'''
Define a function is_palindrome() that recognizes palindromes (that is, words that 
have the same appearance spelled backwards), example: is_palindrome ("radar") would have 
to return True.
'''

def is_palindrome(string):
    backwardsWord = ''
    for i in range(len(string)):
        backwardsWord = string[i] + backwardsWord
    return (string==backwardsWord)

print("Is 'radar' a palindrome?", is_palindrome('radar'), "\nIs 'hello' a palindrome?", is_palindrome('hello'))
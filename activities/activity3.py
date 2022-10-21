'''
Write a function that takes a character and returns True if it is a vowel, otherwise
returns False.
'''

def isVowel(character):
    if(character=='a'or character=='e' or character=='i' or character=='o' or character=='u'):
        boole = True
    else:
        boole = False

    return boole

print("Is 'E' a vowel?", isVowel('e'))
print("Is 'S' a vowel?", isVowel('s'))

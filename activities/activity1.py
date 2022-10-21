'''
Define a max() function that takes two numbers as an argument and returns the
bigger of them. (It's true that python has a built-in max() function, but making it
ourselves is a very good exercise.
'''

def max(number1, number2):
    if(number1>number2):
        max = number1
    else:
        max= number2
    return max

print("The biggest is", max(4,3))
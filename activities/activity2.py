'''
Define a function max_of_three(), which takes three numbers as arguments and returns the
biggest of them. 
'''

def max_of_three(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            max = num1
        else:
            max = num3
    else:
        if(num2>num3):
            max = num2
        else:
            max = num3
    return max

print('The biggest is:', max_of_three(2,3,1))


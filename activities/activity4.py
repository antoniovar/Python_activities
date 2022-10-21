'''
Write a sum() function and a multip() function that add and multiply, respectively, all 
the numbers in a list. For example: sum([1,2,3,4]) should return 10 a nd multip([1,2,3,4]) 
should return 24.
'''
#Sum function
def sum(list):
    total_sum = 0
    for i in list:
        total_sum += i
    return(total_sum)

#Multip function
def multip(list):
    total_multip = 1
    for i in list:
        total_multip *= i
    return(total_multip)


print("With the array [1,2,3,4] sum returns:", sum([1,2,3,4]), 
'and with same array multip returns:', multip([1,2,3,4]))
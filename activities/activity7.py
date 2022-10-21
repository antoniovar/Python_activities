'''
Define an overlay() function that takes two lists and returns True if they have 
at least 1 member in common, or returns False otherwise.
Write the function using the nested for loop.
'''

def overlay(list1, list2):
    any = False
    i=0
    while any==False and i<len(list1):
        for j in list2:
            if list1[i]==j:
                any=True
        i+=1
    return any
        

print("Is there an overlay between '[23,43,21]' and '[1,2,3,4,5,6,7,21]'?", overlay([23,43,21], [1,2,3,4,5,6,7,21]),
"\nAnd between '[23,43,21]' and '[1,2,3,4,5,6,7,231]'?", overlay([23,43,21], [1,2,3,4,5,6,7,231]))
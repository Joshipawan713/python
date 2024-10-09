# Recursion - when a function calls itself repeatedly.
# recursion just like loop 

# def show(n):
#     if(n==0): #base case recursion will end or not.
#         return
#     print(n)
#     show(n-1)
    
# show(5)

# factorial number
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(6))
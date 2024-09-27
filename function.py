# function - block of statement that perform a specific task
# def function_name(param1,param2):
#     #some work
#     return val

# def helloprint():
#     print("Hello World")
    
# output = helloprint()
# print(output) # none


# def cal_sum(a,b): #parameters
#     return a + b
    
# sum = cal_sum(1,2) #function call; argument
# print(sum)

# function in python - 1. built in function, 2.user defined function
# 1.built in function - print() , len(), type(), range()
# 2. user defined function - helloprint(), average(), cal_sum()

# Default parameter - assigning a default value to parameter, which is used when no argument is passed.
def cal_prod(a=1,b=1): #default value
    print(a*b)
    return a * b

cal_prod()
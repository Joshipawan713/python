# function
# # 1.average of 3 numbers

# def average(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg


# avg = average(12,15,18)
# print(avg)

# # 2.write a function print the length of a list (list is the parameter)

# def print_len(list):
#     print(len(list))    

# cities = ["delhi","noida","uttar pradesh","uttarkhand"]
# num = [12,15,78,52,65,85]
# print_len(cities)
# print_len(num)

# # 3.write a function to print the element of a list in a single line. (list is the parameter)

# cities = ["delhi","noida","uttar pradesh","uttarkhand"]
# num = [12,15,78,52,65,85]

# def print_list(list):
#     for item in list:
#         print(item,end=" ")
        
# print_list(num)
# print()
# print_list(cities)

# # 4.write a function to find the factorial of n. (n is the parameter)

# def factorial(n):
#     fac = 1
#     for x in range(1,n+1):
#         fac*=x
#     print(fac)
    
# n = 6
# factorial(n)

# # 5.write a function to convert usd to inr.

# def usd_inr(con):
#     return con * 80

# usd = 10
# inr = usd_inr(usd)
# print(inr)


# def usd_inr(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD =", inr_val, "INR")
    
# usd_inr(73)

# write a function give a input and return if input is odd then print "ODD" otherwise print "Even"

def odd_even(input):
    if(input %2 == 0):
        print("EVEN")
    elif(input %2 != 0):
        print("ODD")
    else:
        print("Please Enter input")
        
odd_even(2)


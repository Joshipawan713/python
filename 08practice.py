# for loops
# # 1.print the element of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

# list = [1,4,9,16,25,36,49,64,81,100]
# for x in list:
#     print(x)

# # 2.search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]
# num = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx=0

# for el in num:
#     if(el == x):
#         print("number found at idx", idx)
#         break
#     idx+=1

# # 3.even number print by using for loop
# for i in range(2,20,2):
#     print(i)
    
# # 4.odd number print by using for loop
# for i in range(1,20,2):
#     print(i)

# 5.print number from 1 to 100

# for x in range(1,101):
#     print(x)

# 6.print number from 100 to 1

# for y in range(100,0,-1):
#     print(y)

# # 7.print the multiplication table of a number n.
# num=int(input("Enter The number : "))
# for i in range(1,11):
#     print(i*num)

# 8.write a program find the sum of first n numbers (using while)

# # while method
# n=5
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
    
# print("total sum=",sum)

# # for method 
# n=6
# sum=0
# for i in range(1,n+1):
#     sum +=i

# print("total sum =",sum)

# 9.write a program the factorial of first n numbers. (using for)
# # while method
# n=3
# fac=1
# i=1
# while i<=n:
#     fac=fac*i
#     i+=1

# print("total factorial=",fac)

# for method
n=5
fac=1
for i in range(1,n+1):
    fac*=i
    
print("total factorial=",fac)

# lecture 6 - start video
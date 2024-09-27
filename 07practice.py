# while loop
# 1. print number from 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i+=1

# 2. print number from 100 to 1

# i=100
# while i>=1:
#     print(i)
#     i-=1

# 3. print the multiplication table of a number n.

# n=int(input("Enter the table : "))
# i=1
# while i<=10:
#     print(n,"X",i,"=",n*i)
#     i+=1

# 4. print the element of the following list using a loop:
# [4,4,9,16,25,36,49,64,81,100]

# list = [4,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(list):
#     print(list[idx])
#     idx+=1


# 5. search for a number x in this tuple using loop
# (4,4,9,16,25,36,49,64,81,100)

tup = (4,4,9,16,25,36,49,64,81,100)
search = 25
i=0 # initialization
while i<len(tup):
    # print(tup[i])
    if(tup[i]==search):
        print("found",i)
    else:
        print("finding..")
    i+=1
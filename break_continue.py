# break and continue
# break used to terminate the loop when encountered.
# continue terminates execution in the current iteration & continues execution of the loop with the next iteration.

# i=1
# while i<5:
#     print(i)
#     if(i==3):
#         break
#     i+=1

# tup = (4,4,9,16,25,36,49,64,81,100)
# search = 25
# i=0 # initialization
# while i<len(tup):
#     # print(tup[i])
#     if(tup[i]==search):
#         print("found",i)
#         break
#     else:
#         print("finding..")
#     i+=1
# print("end of loop")

#continue
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue #skip
    print(i)
    i+=1
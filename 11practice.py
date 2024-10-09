# # file practice
# # 1. create a new file "practice.txt" using python. add the following data in it.
# # hi everyone
# # we are learning file I/O
# # using Java
# # I like programming in Java

# with open('practice.txt','w') as f:
#     f.write("hi everyone\nwe are learning file I/O\n")
#     f.write("using Java\nI like programming in Java")

# # 2. write a function that replaces all occurrence of "java" with "python" in above files.
# with open('practice.txt','r') as f:
#     data = f.read()
    
# newdata=data.replace('Java','Python')
# print(newdata)

# with open('practice.txt','w') as f:
#     f.write(newdata)

# # 3. search if the word "learning" exists in the file or not
# word = "learning"
# with open('practice.txt','r') as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")

# # through function
# def check_for_word():
#     word = "learning"
#     with open('practice.txt','r') as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")
            
# check_for_word()

# # write a function in which line of the file does the word "learning" occur first.
# # print -1 if word not found
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
#     return -1
# check_for_line()

# from a file containing numbers separated by comma, print the count of even numbers.
# 1,2,76,84,90,101
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ','):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
    
    nums = data.split(",")
    for val in nums:
        if(int(val)% 2 == 0):
            count +=1
print(count)
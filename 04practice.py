# list practice set
# 1. write a program to ask the user to enter names of their 3 favorite movie and store them in a list
movies = []
# #first method to solve this question
# mov1 = input("Enter First Movie Name : ")
# mov2 = input("Enter Second Movie Name : ")
# mov3 = input("Enter Third Movie Name : ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# #second method to solve this question
# movies.append(input("Enter First Movie Name : "))
# movies.append(input("Enter First Movie Name : "))
# movies.append(input("Enter First Movie Name : "))

# print(movies)

# 2. write a program if a list contains a palindrome of element (hint use copy() method)
# palindrome - start read same list or contain and end to read same like - [1,2,3,2,1] , [1,"abc","abc",1]

# list1 = [1,2,1]
# list1 = ["m","a","a","p"]
# # list2 = [1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palindrome")

# tuple practice set
# 1. write a program count of the number of student with the "A" grade in the following tuple
# ["C","D","A","A","B","B","A"]

# grade = ("C","D","A","A","B","B","A")
# print(tup.count("A"))


# 2. store the above value in a list & sort them from "A" to "D"
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)
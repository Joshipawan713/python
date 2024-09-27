# 1. store following word meaningful in a python dictionery : 
# table : "a piece of furniture", "list of facts & figure"
# cat : "a small animal"

# dictionery = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figure"]
# }

# print(dictionery)

# 2. you are given a list of subject for students. Assume one classroom is required for 1 subject. How many classroom are needed by all students.
# "python","java","c++","python","javascript",
# "java","python","java","c++","c"

# subject = {
#     "python","java","c++","python","javascript","java","python","java","c++","c"
# }

# print(subject)
# print(len(subject))

# 3. write a program of 3 subject from the user and store them in a dictionery . start with an empty dictionery and add one by one . use subject
# name as key & marks as value
# marks = {}
# x = int(input("Enter account : "))
# marks.update({"account":x})
# x = int(input("Enter business : "))
# marks.update({"business":x})
# x = int(input("Enter economics : "))
# marks.update({"economics":x})

# print(marks)

# 4. figure out a way to store 9 & 9.0 as separate value in the set.(yoy can help of built-in data type)

# value = {9,9.25,8,8.0,"8.0"} # 8 and 8.0 are same then this case python 8 print but 8 and "8.0" python treat different because "8.0" is string.
# print(value)

value = {
    ("float",9.0),
    ("int",9)
}

print(value)
# string
# basic operator

# 1. Concatenation
# str1 = "Hello"
# str2 = "World"
# str3 = str1+" "+str2
# print(str3)

# 2. length of string - len(str) - len count space and space squence character
# str4 = "Hello World"
# lenstr = len(str4)
# print(lenstr)

# 3. indexing
# str1 = "Hello World"
# ch = str1[0]
# print(ch)

# 4. slicing - accessing part of string. divide a part of string
# str = "Hello World"
# print(str[1:5]) #not include 5 only return 4 value
# print(str[1:len(str)]) #[0:11]
# print(str[1:]) #ending value not given the program read length of str [1:11]
# print(str[:4]) #starting value not given the program read 0 [0:4]

# 5.slicing - negative index
# str = "Apple"
# print(str[-3:-1]) #print - (pl)

# 4. string some other function
str = "i am from studying python from ApnaCollege"
# str.endswith("ege") #return true if string ends with substr
# str.capitalize() #captalize 1st char
# str.replace(old,new) #replaces all occurrence of old with new
# str.find() #return 1st index of 1st occurrence
# str.count() #counts the occurrence of substr in string

# print(str.endswith("ege")) #return true
# print(str.endswith("pnaC")) #return false
# print(str.capitalize())
# print(str.replace("o","a"))
# print(str.replace("python","javascript"))
# print(str.find("o")) #if string or charcter not exist in output return -1 or negative value
# print(str.count("o"))
print(str.count("from"))
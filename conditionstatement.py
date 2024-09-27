# conditional statement
# syntax - if-elif-else

#traffice light porgram
# light = "blue"
# if(light == "red"):
#     print("Stop") #space for print indentation
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")

#grade based student marks
# marks = int(input("Enter Mraks : "))
# if(marks >=90):
#     print("A")
# elif(marks>=80 and marks<90):
#     print("B")
# elif(marks>=70 and marks<80):
#     print("C")
# elif(marks>=55 and marks<70):
#     print("D")
# else:
#     print("E")

age = 81

#nesting if statement
if(age>=18):
    if(age >=80):
        print("cannot drive")
    else:
        print("You can drive")
else:
    print("You can not drive")
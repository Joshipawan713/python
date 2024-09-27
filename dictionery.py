# dictionary in python - dictionaries are used to store data values in key:value pairs
# they are unordered, mutable(changable) & donot allow duplicate keys

dict = {} #this is empty dictionery

# dict = {
#     "key" : "value",
#     "name" : "python",
#     "learning" : "coding",
#     "age" : 35,
#     "marks" : 94,
#     "subject" : ["python","c","c++","javascript"],
#     "topics" : ("dict","set"),
#     12 : 12
# }
# # print(dict["name"])
# # print(dict["subject"])

# dict["name"] = "dictname"
# dict["newname"] = "add_new_value" # add new key and value
# print(dict)

# nested dictionery
# student = {
#     "name" : "raj",
#     "subject" : {
#         "acc" : 37,
#         "bus" : 45,
#         "eco" : 45
#     }
# }

# print(student["subject"]["acc"])

# lecture - 4 - 14:26 last video

# dictionery methods
# mydict.keys() #returns all keys
# mydict.values() #returns all values
# mydict.items() #return all (key, val) pairs as tuples
# mydict.get("key") #return the key according to value
# mydict.update(newdict) #insert the specified item to the dictionery

student = {
    "name" : "raj",
    "subject" : {
        "acc" : 37,
        "bus" : 45,
        "eco" : 45
    }
}

# print(list(student.keys())) #change data type with type casting
# print(len(list(student.keys()))) #change data type with type casting and print the length of key
# print(list(student.values()))
# pairs = list(student.items()) #return tuple value
# print(pairs[1]) #return tuple value
# print(student["name2"]) #return error print
# print(student.get("name2")) #return none

newdict = {"name":"abc","city":"delhi", "age":16} #name is overwrite
student.update(newdict)
print(student)

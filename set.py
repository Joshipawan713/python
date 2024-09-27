# set in python - set is the collection of the unordered items. each element in the set must be unique and immutable.
# store in set -  boolen , int , float , str, tuple
# they can not store in set - list and dictionery

# collection = set() # empty set 
# print(type(collection))

# # collection = {1,2,3,4,2,"hello","world","world"} # set ignore duplicate value only single read
# print(collection)
# print((len(collection))) #total number of item

# set method
# set.add(element) # add an element
# set.remove(element) # removes the element
# set.clear() #empties the set
# set.pop() #removes a random value
# set.union(set2) #combines both set value & return new
# set.intersection(set2) #combines common value and return new

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2) #not read duplicate value
# collection.add("hello")
# collection.add("world")
# collection.add((1,2,3,4))

# # collection.remove(1)
# collection.clear()

# print(len(collection))

# collection = {"hello","world","python","java","javascript","html","css"}
# print(collection.pop()) #random value generate

set1 = {1,2,3}
set2 = {2,3,4}
# print(set1.union(set2)) #{1,2,3,4}
print(set1.intersection(set2)) #{2,3}
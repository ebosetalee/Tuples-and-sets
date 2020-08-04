# The shelve module provides a shelve (like a dictionary) but stored in
# a file rather than in memory. Like a dictionary, the shelve holds key 
# value pairs and the values can be anything (pickled). The keys themselves
# must be strings unlike a dictionary where the keys can be immutable 
# objects such as tuples.
# All the methods used with dictionaries can be used for shelve objects. 
# Thus, can be called persistent dictionary. It is easy to convert code 
# using a dictionary to use a shelve instead because the values are pickled
# when saved. NOte loading a shelve can execute code like pickle.
#  
import shelve

with shelve.open("shelfTest") as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "Good for making Cider" 
    fruit["lemon"] = "A sour, yellow citrus fruit"
    fruit["grape"] = "A small, sweet fruit growing in bunches" 
    fruit["lime"] = "A sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])
    
# It's seen that we open a shelve the same way we open a file using with,
# but no need to specify the mode or write or read. 

# Note it is stored in .db extension, python uses a database to store the data
# and pickled the values so that complex python structures can be stored as 
# database fields.
# So the databased used depends on the underlying python implementation. once 
# its open, we can use it like a dictionary.
# 
# The difference between shelve and dictionary is that there's no shelve literal
# As seen below:

# with shelve.open("shelfTest") as fruit:
#     fruit = {"orange": "a sweet, orange, citrus fruit",
#             "apple": "Good for making Cider", 
#             "lemon": "A sour, yellow citrus fruit",
#             "grape": "A small, sweet fruit growing in bunches", 
#             "lime": "A sour, green citrus fruit"}

# print(fruit["lemon"])
# print(fruit["grape"])

# if we run this:
# print(fruit) # prints a dictionary.

print(fruit) # prints a shelve

# if they aren't indented, we get an error
# print(fruit["lemon"])
# print(fruit["grape"])

# To not bother about indentation due to the with method that closes
# the file, we can use the following:

# fruit = shelve.open("shelfTest") 
# fruit["orange"] = "a sweet, orange, citrus fruit"
# fruit["apple"] = "Good for making Cider" 
# fruit["lemon"] = "A sour, yellow citrus fruit"
# fruit["grape"] = "A small, sweet fruit growing in bunches" 
# fruit["lime"] = "A sour, green citrus fruit"

# fruit.close()

# print(fruit["lemon"])
# print(fruit["grape"])
# No identation needed.
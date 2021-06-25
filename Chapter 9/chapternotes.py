# A dictionary is an object that stores a collection of data.
# Each element in a disctionary has two parts:
# A key, and a value
# You use a key to locate a specific value.
# for example, a dictionary. When you want to locate the meaning of a word,
# you locate the word in the dictionary to find its definition.
# Dictionary elements are commonly referred to as Key-value pairs.
# When you want to retrieve a specific value from a dictionary, you use the key
# that is associated with that value.
# Key-value pairs are often referred to as mappings because each key is mapped to a value.
# You create a dictionary by enclosing the elements inside with {}.
# an element consists of a key, followed by a colon, followed by a value.
# elements are seperated by commas
# phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
# In this example, the keys and values are strings.
# values in a dictionary can be objects of any type, but the keys must be immutable objects.
# for example keys can be strings, integers, floats, or tuples.
# Keys cannot be lists or any other tupe of immutable object.
# IMPORTANT: Disctionaries are not sequences, like lists, tuples, and strings.
# as a result, you cannot use a numeric index to retrieve a value from a dictionary
# instead, you use a key to retrieve a value
# To retrieve a value, you simply write an expression in the following format:
# dictionary_name[key]
# If the key entered does not exist, it will through a KeyError exception
# Note; string comparisons are case sensitive
# to prevent a KeyError exception, you can use the *in* operator to
# determine whether a key exists before you try to retrieve a value
# you can also use the *not in* operator

# Dictionaries are mutable objects.
# You can add new key-value pairs to a dictionary with the format:
# dictionary_name[key] = value
# If key already exists in the dictionary, its value will be changed to value in format.
# If the key does not exist, it will be added to the dictionary along with its value.
# NOTE: You cannot have duplicate keys in a dictionary

# you can also delete existing key-value pairs with the *del* statement
# del dictionary_name[key]
# after that executes, the key and its value will be deleted.
# if the key does not exist, a KeyError exception is raised.
# You can also use the *in* operator to see if the key exists

# You can use the *len* function to retrieve the number of elements in a dictionary
# num_items = len(dictionary_name)

# As mentioned before, keys in a dictionary must be immutable objects
# But their associated values can be any type of object.
# For example, the values can be lists
# test_scores = { 'Kayla' : [88, 92, 100], 2                'Luis' : [95, 74, 81], 3                'Sophie' : [72, 88, 91], 4                'Ethan' : [70, 75, 78] }
# Also, values that are stored in a single dictionary can be of different types
# For example, one elements value might be a string, another a list, and another an integer.
# Keys can also be of different types, aslong as they are immutable.

# sometimes, you need to create an empty dictionary and then add elements
# to it as the program executes.
# dictionary_name = {}
# you can also use the built-in dict() method to create an empty dictionary
# dictionary_name = dict()

# You can also use a for loop to iterate over a dictionary
# for var in dictionary:
#   statement
#   statement
#   etc.
# in general, var is the name of a variable and dictionary is the name of the dictionary
# this loop iterates once for each element in the dictionary
# each time the loop iterates, var is assigned to a key.
# for key in dictionary:
#   print(key, phonebook[key])
# this will print both the key and its value for each element in the dictionary

# some important dictionary methods
# clear: Clears the contents of a dictionary
# get: gets the value associated with a specified key. If the keys is not found
# the method does not raise an exception. Instead, it returns a default value
# items: returns all the keys in a dictionary and their associated values as a sequence of tuples
# keys: Returns all the keys in a dictionary as a sequence of tuples.
# pop: returns the value associated with a specified key and removes that key-value pair from
# the dictionary. If the key is not found, the method returns a default value
# popitem: returns a randomly selected key-value pair as a tuple from the dict
# and removes that pair from the dictionary
# values: Returns all the values in the dictionary as a sequence of tuples

# the clear method deletes all the elements in a dictionary, leaving it empty.
# dictionary.clear()

# the get method
# dictionary.get(key, default)
# the word default is the value to return if the key is not found

# for key, value in phonebook.items():
#   print(key, value)
# items() returns a sequence of tuples containing the dict's pairs

# if we call the phonebook.keys() method, it will return all of the keys in a list.
# for key in phonebook.keys():
#   print(key)

# dictionary.pop(key, default)
# if key is not found return value: default
# phone_num = phonebook.pop('Chris', 'Entry not found')
# phone_num >> 555-1111
# but not the key value pair is erased from the dict

# k, v = dictionary.popitem()
# a randomly selected pair is erased from the dictionary
# but the key is assigned to k, the the value to v
# this is called multiple assignment

# for val in phonebook.values():
#   print(val)
# this prints all of the values from the dictionary



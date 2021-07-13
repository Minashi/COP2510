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

# --------------------------------------------------------------------------------

# A set contains a collection of unique values and works like a mathematical set
# Important:
# 1. All elements in a set must be unique. No two elements can have the same value
# 2. Sets are unordered, which means that the elements in a set are not stored in any particular order.
# 3. The elements that are stored in a set can be of different data types.

# To create a set, call the built-in set function.
# myset = set()
# you can also set arguments in the function.
# the argument you pass must be an object that contains iterable elements
# such as a list, a tuple, or a string.
# myset = set(['a', 'b', 'c'])
# Is that example, we are passing a list as an argument to the set function.
# the myset variable not references a set containing the elements a, b, and c.
# if you pass a string as an argument to the set function, each character in the string
# becomes a member of the set.
# myset = set('abc')
# myset now references a set containing the elements a, b, and c.
# Sets also cannot contain duplicate elements.
# if you try this: myset = set('aaabc')
# a only appears once in the set, so myset references a, b, and c.

# what if you want to create a set were each element is a string with more then 1 letter?
# this won't work: myset = set('one', 'two', 'three')
# you can to pass the argument as a list
# myset = set(['one', 'two', 'three'])

# as with lists, tuples, and dictionairs, you can use the len function
# to get the number of elements in a set.
# myset = set([1, 2, 3, 4, 5])
# len(myset)
# 5

# sets are mutable objects, so you can add items and remove items from them.
# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(3)
# myset
# {1, 2, 3}
# myset.add(2)
# myset
# {1, 2, 3}

# You can add a group of elements to a set at one time with the update method.
# myset = set([1, 2, 3])
# myset.update([4, 5, 6])
# myset
# {1, 2, 3, 4, 5, 6}

# You can also update a set with a set.
# myset1 = set([1, 2, 3])
# myset2 = set([8, 9, 10])
# myset1.update(myset2)
# myset1
# {1, 2, 3, 8, 9, 10}
# myset2
# {8, 9, 10}

# You can remove an item from a set with either the remove method, or the discard method
# the remove method raises a KeyError exception
# the discard method does not raise an exception

# you can also clear all the elements of a set by calling the clear method
# myset.clear()

# you can use the for loop to iterate over all the elements in a set
# for var in set:
#   statement
#   statement
#   etc.
# in general format, var is the name of a variable
# and set is the name of the set.
# myset = set(['a', 'b', 'c'])
# for val in myset:
# print(val)
# a
# c
# b

# you can also use the in and not in operators to test
# a value in a set

# The UNION of two sets is a set that contains all the elements
# in both sets.
# set1.union(set2)

# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set1.union(set2)
# set3
# {1, 2, 3, 4, 5, 6}
# you can also use the | operator to find the union of two sets
# set3 = set1 | set2
# set3
# {1, 2, 3, 4, 5, 6}

# The intersection of two sets is a set that contains only
# the elements that are found in both sets.
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set1.intersection(set2)
# set3
# {3, 4}
# you can also use the & operator to find the intersection of two sets
# set3 = set1 & set2

# You can also find the difference between 2 sets.
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set1.difference(set2)
# set3
# {1, 2}
# You can also do this with the - operator
# set3 = set1 - set2

# You can also find the symmetric difference of two sets
# that contains elements that are not shared by the sets.
# in other words, it is the elements that are in one set but not both
# you must call the symmetric_difference method
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set1.symmetric_difference(set2)
# set3
# {1, 2, 5, 6}
# you can also do this with the ^ operator
# set1 ^ set2

# SUBSETS AND SUPERSETS
# Suppose you have two sets, and one of those sets contains all of the
# other elements of the other set. EXAMPLE:
# set1 = set([1, 2, 3, 4])
# set2 = set([2, 3]
# In this example, set1 contains all the elements of set2.
# This means that set2 is a SUBSET of set1.
# This also means that set1 is a SUPERSET of set2.
# in python, you can call the issubset method to determine
# whether one set is a supset of another
# set2.issubset(set1)
# this returns true if set2 is a subset of set1.
# You can also call the issuperset method
# set1.issuperset(set2)
# method returns true if set1 is a superset of set2
# You can also use the <= operator to determine whether
# one set is a subset of another, and the >= operator
# to determine whether one set is a superset of another
# set2 <= set1
# set1 >= set2

# SERIALIZING OBJECTS
# Serializing an object is the process of converting
# the object to a stream of bytes that can be saved
# to a file for later retrieval. In python
# object serialization is called pickling

# in chapter 6 I learned how to store data in a text file
# sometimes, you need to store the contents of a complex
# object, such as a dictionary or a set, to a file.
# the easiest way to save an object to a file is to
# serialize the object.
# The python standard library provides a module named
# pickle that has various functions for serializing
# or (pickling) objects.

# Once you import the pickle module, you perform the
# following steps to pickle an object.
# 1. You open a file for binary writing
# 2. you call the pickle module's dump method to pickle
# the object and write it to the specified file
# 3. after you have pickled all the objects, close the file.

# STEP 1
# to open a file for binary writing, you use wb and the mode when
# you call the open function
# outputfile = open('mydata.dat', 'wb')

# once you have opened the file for binary writing, you
# call the pickle module's dump function.
# pickle.dump(object, file)
# in general format, object is a variable that references
# the object you want to pickle, and file is a variable
# that references the file object
# after the function executes, the object referenced
# will be serialized and written to the file.
# you can pickle about any type of object, including
# lists, tuples, dictionaries, sets, strings, integers, and floats
# you can save as many pickld objects to a file that you want
# when finished, call the close method to close the file.

# EXAMPLE:
# import pickle
# phonebook = {'Chris' : '555−1111',
#              'Katie' : '555−2222',
#              'Joanne' : '555−3333'}
# output_file = open('phonebook.dat', 'wb')
# pickle.dump(phonebook, output_file)
# output_file.close()

# HOW TO OPEN/READ PICKLED FILES
# To open a file for binary reading, you use the 'rb'
# as the mode when you call the open function.
# inputfile = open('mydata.dat', 'rb')
# then you call the pickle module's load function.
# object = pickle.load(file)
# after the function executes, the object variable
# will reference an object that was retrieved from the
# file and unpickled.
# You can unpickle as many objects as necessary form the file.
# (If you try to read past the end of the file, the
# load function will raise an EOFError exception)
# when finished, call the objects close method

# EXAMPLE:
# import pickle
# input_file = open('phonebook.dat', 'rb')
# pb = pickle.load(inputfile)
# pb
# {'Chris': '555−1111', 'Joanne': '555−3333', 'Katie': '555−2222'}
# input_file.close()







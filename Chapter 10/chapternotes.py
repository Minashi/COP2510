# 10.1 PROCEDURAL AND OBJECT-ORIENTED PROGRAMMING

# CONCEPT:
# Procedural programming is a method of writing software.
# It is a programming practice centered on the procedures
# or actions that take place in a program.
# Object-oriented programming is centered on objects. Objects
# are created from abstract data types that encapsulate data
# and functions together.

# There are primarily two methods of programming in use today
# 1. Procedural & 2. Object-Oriented
# The earliest programming languages were procedural,
# meaning a program was made of one or more procedures.
# you can think of a procedure simply as a function that
# performs a specific task such as gathering input from the
# user, performing calculations, reading or writing files
# displaying output, and so on.
# The programs that I have written so far have been procedural in nature.

# Whereas procedural programming is centered on creating procedures
# (functions), OOP is centered on creating objects.
# An object is a software entity that contains both data and
# procedures.
# The data contained in an object is known as the object's
# Data attributes.
# An objects data attributes are simply variables that reference
# data.
# The procedures tat an object performs are known as methods.
# an objects methods are functions that perform operations on the
# objects data attributes. The object is, conceptually, a
# self-contained unit that consists of data attributes and
# methods that operate on the data attributes.

# OOP addresses the problem of code and data separation through
# encapsulation and data hiding.
# Encapsulation refers to the combining of data and code into
# a single object.
# Data hiding refers to an object's ability to hide its data attributes
# from the code that is outside the object.
# Only the object's methods may directly access and make changes
# to the object's data attributes.
# an object typically hides its data, but allows outside code
# to access its methods.

# When an object's data attributes are hidden from outside code,
# and access to the data attributes is restricted to the objects
# methods, the data attributes are protected from accidental corruption
# Inaddition, the code outside the object does not need to know about
# the format or internal structure ofthe object’s data.
# The code only needs to interact with the objects methods.
# When a programmer changes the structure of an objects internal
# data attributes, he or she also modifies the object's methods
# so they may properly operate on the data. The way in which
# outside code interacts with the methods, however, does not change.

# OBJECT REUSABILITY
# OOP has also been encouraged by the trend of object reusability.
# an object is not a stand-alone program, but is used by programs
# that need its services.

# Methods that can be accessed by entities outside the object
# are known as public methods
# There are also private methods, which are part of the objects
# private, internal working.

# 10.2 CLASSES
# CONCEPT:
# A class is code that specifies the data attributes and
# methods for a particular type of object.

# To create a class, you write a class definition.
# A class definition is a set of statements that define a class's
# methods and data attributes.

# To make an attribute private, add __ behind the attribute.
# self.__face = 'heads'

# 10.3 WORKING WITH INSTANCES
# tomorrow write notes on 'getters' and 'setters'
# Each instance of a class has its own set of data attributes.
# When a method uses the self parameter to create an attribute,
# the attribute belongs to the specific object that self references.
# We call these attributes instance attributes because they
# belong to a specific instance of the class.
# Its possible to create many instances of the same class in a program.
# Each instance will then have its own set of attributes.

# It is common practice to make all of a class's data attributes private,
# and to provide public methods for accessing and changing those attributes.
# This ensures that the object owning those attributes is in control of all the changes being
# made to them.
# A method that returns a value from a class's attribute but does not
# change it is known as an accessor method.
# Accessor methods provide a safe way for code outside the class
# to retrieve the values of attributes, without exposing the
# attributes in a way that could be changed by the code outside
# the method.

# A method that stores a value in a data attribute or changes the value
# of a data attribute in some other way is known as a mutator method.
# Mutator methods can control the way that a class's data attributes
# are modified.
# When code outside the class needs to change the value of an object's data attribute,
# it typically calls a mutator and passes the new value as an argument.
# If necessary, the mutator can validate the value before it assigns it to the data attribute.

# Mutator methods are sometimes called 'setters' and accessor
# methods are sometimes called 'getters.'

# You can also store objects into a list.

# OBJECTS IN A LIST
#

# PASSING OBJECTS AS ARGUMENTS
# You often need to write functions and methods that
# accept objects as arguments.
# When you pass an object as an argument, the thing that is passed into
# the parameter variable is a reference to the object.
# as a result, the function or method that receives the object
# as an argument has access to the actual object.
# EXAMPLE:
# def flip(coin_obj)
#       coin_obj.toss()

# Recall that the pickle module provides functions for
# serializing objects.
# Doing so converts it into a stream of bytes that can
# be saved to a file for later retrieval.

# The pickle module's dump function serializes an object
# and writes it to a file, and the load function retrieves an object
# from a file and deserializes (unpickles) it.
# NOTE: I recommend making a constant variable for a file name.

# You can also store objects in a DICTIONARY

# TECHNIQUES FOR DESIGNING CLASSES
# When designing a class, it is often helpful to draw a
# UML diagram.
# UML stands for Unified Modeling Language.
# It provides a set of standard diagrams for graphically
# depicting object-oriented systems.
# The diagram is a box that is divided into three sections.
# The TOP section is where you write the name of the class.
# The middle section holds a list of the class's attributes.
# the bottom section holds a list of the class's methods.

# When developing an OOP, one of your first tasks is to
# identify the classes that you will need to create.
# Typically, your goal is to identify the different types
# of real-world objects that are present in the problem, then
# create classes for those types of objects within your application

# One simple and popular technique involves the following steps:
# 1. Get a written description of the problem domain
# 2. Identify all the nouns (including pronouncs and noun phrases)
# in the description.
# Each of these is a potential class.
# 3. Refind the list to include only the classes that are
# relevant to the problem.

# The PROBLEM DOMAIN is the set of real-world objects, parties
# and major events related to the problem.
# If you adequately understand the nature of the problem
# you're trying to solve, you can write a description of the
# problem domain yourself.
# If you do not thoroughly understand the nature of the problem
# you should have an expert write the description for you

# EXAMPLE
# Joe’s Automotive Shop services foreign cars and specializes in servicing cars made by
# Mercedes, Porsche, and BMW. When a customer brings a car to the shop,
# the manager gets thecustomer’s name, address, and telephone number.
# The manager then determines the make,model, and year of the car and gives the customer a service quote.
# The service quote shows theestimated parts charges,
# estimated labor charges, sales tax, and total estimated charges.

# The problem domain description should include any of the following:
# physical objects such as vehicals, machines, or products.
# any role played by a person, such as a manager, employee,
# customer, teacher, student, etc.
# The results of a business event, such as a customer order
# or in this case a service quote.
# Recordkeeping items, such as customer histories and payroll records

# IDENTIFY ALL OF THE NOUNS
# notice some of the nouns are repeated.
# Address, BMW, Car, Cars, customer, estimated labor charged
# estimated parts charges, foreign cars, Joe's Automotive Shop
# make, manager, mercedes, model, name, Porsche, sales tax
# service quote, shop, telephone number, total estimated charges
# year.

# REFINING THE LIST
# The nouns that appear in the description are merely candidates
# to become classes.
# It might not be necessary to make classes for them all.
# The next step is to refind the list to incllude only
# the classes that are necessary to solve the particular problem
# at hand.
# Common reasons a noun can be eliminated from the list:
# car, cars, and foreign cars. (These all refer to the general
# concept of a car)
# Joe's automotive shop and shop
# (Both of these refer to the company)

# We can settle on a single class for each of these.
# The updated list of potential classes is:
# Address, BMW, car, customer, estimated labor charges,
# estimated parts charges, make, manager, mercedes, model
# name, porsche, sales tax, service quote, shop, telephone number
# total estimated charges, year

# some nouns might represent items that we do not need
# to be concerned with in order to solve the problem.
# A quick review of the problem description reminds us
# of what our application should do:
# print a service quote.

# in this example, we can eliminate two unnecessary classes
# from the list.
# we can remove 'shop' off the list because our application
# only needs to be concerned with individual service quotes.
# it doesn't need to work with or determine any company-wide
# information.
# If the problem desc. asked us to keep a total of all the
# service quotes, then it would make sense to have a class
# for the shop.

# We will not need a class for the manager because the
# problem statement does not direct us to process any information about
# the manager.
# If there were multiple shop managers, and the problem desc.
# had asked us to record which manager generated each service
# quote, then it would make sense to have a class for the manager.

# The updated list of potential classes:
# Address, BMW, car, customer, estimated labor charges,
# estimated parts charges, make, Mercedes, model, name
# Porsche, sales tax, service quote, telephone number,
# total estimated charges, and year.

# Some of the nouns might represent objects, not classes.
# We can remove Mercades, Porsche, and BMW as classes, in
# this example, they all represent specific cars and can be
# considered instances of a car class.
# UPDATED LIST:
# Address, car, customer, estimated labor charges,
# estimated parts charges, make, model, name, sales tax
# service quote, telephone number, total estimated charges
# and year.

# Some OO designers take note of whether a noun is plural or
# singular. Sometimes a plural noun will indicate a class, and
# a singlular noun will indicate an object.
# Some of the nouns might represent simple values that can
# be assigned to a variable and do not require a class.
# Remember, a class contains data attributes and methods.
# If a noun represents a type of item that would not
# have any identifiable data attributes or methods, then
# it can probably be eliminated from the list.

# To help determine whether a noun represents an item that would
# have data attributes and methods, ask the following questions about it:
# 1. Would you use a group of related values to represent
# the item's state?
# 2. Are there any obvious actions to be performed by the item?
# If the answer is no to both, then the noun probably
# represents a value that can be stored in a simple variable.
# If we apply this test to each of the nouns that remain in
# our list, we can conclude that the following are probably
# not classes: Address, labor charges, parts charges, make
# model, name, sales tax, tele num, total charges, and year.

# Here is the UPDATED LIST:
# Car, customer, service quote
# This means our application will need classes to represent
# cars, customers, and service quotes. Ultimately, we will
# write a car class, a customer class, and a serviceQuote class.

# IDENTIFYING A CLASS'S RESPONSIBILITIES
# Once the classes have been identifies, the next task is to
# identify each class's responsibilities.
# 1. Things that the class is responsible for knowing
# 2. Actions that the class is responsible for doing

# When you identify the things the class is responsible
# for knowing, then you have identified the class's data
# attributes.
# and for doing, the methods.


# x = "Hello World!"
# print(x)
# y = 42
# print(y)

# import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')


# import random

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')


# x = 10
# if x > 50:
#     print("bigger than 50")
# else:
#     print("smaller than 50")

# class EmptyClass:
#     pass

# for val in my_string:
    # pass

# for val in my_string:
    # pass


# is_hungry = True
# has_freckles = False

# Tuples a type if data that is immutable
# dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])
# dog[1] = 'dachshund'


# List- a type of data that is mutable and can hold a group of values.Usually meant to store a collection of related data
# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2])
# out put will be Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# apend is doing is adding michael to last end of the string>👇
# print(ninjas)
# output: ['Francis','KB', 'Oliver', 'Michael']
# ninjas.pop()
# pop is removing the last index from the string like it removed michael 👇
# print(ninjas)
# output: ['Francis', 'KB', ''Oliver]
# ninjas.pop(1)
# output: it removes the index of 1 which its 'KB'👇
# print(ninjas)
# output: ['Francis', 'Oliver']


# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)  # output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)  # output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)  # output: ['Francis', 'Oliver']

# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'
# new_person['hobbies']= ['climbing','coding'] #this is going to be added at the end after False with square brackets
# print(new_person)
# w = new_person.pop('weigth')
# print(w)
# print(new_person)

# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# updates if the key exists, adds a key-value pair if it doesn't
# new_person['name'] = 'Jack'
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')  # removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

# print(type(2.63))
# print(type(new_person))

# print(type(2.63))		# output: <class 'float'>
# print(type(new_person))		# output: <class 'dict'>

# print(len(new_person))		# output: 4 (the number of key-value pairs)
# print(len('Coding Dojo'))  # output: 11


# print(type(24))
# print(type(3.9))
# print(type(3j))

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# name = 'Jack'
# print('My name is', name)

# name= "Zen"
# print("My name is" +  name)

# age = "30"
# print("My age is", age)

# age = "30"
# print("My age is"+age)

# total = 35
# user_val = "26"
# total = total + user_val
# total = total + int(user_val)

# total = 35
# user_val = "26"
# total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61


# print("Hello" +42)
# print("Hello" + str (42))

first_name = "Zen"
last_name = "Coder"
age = 27 
print(f"My name is {first_name} {last_name} and I am {age} years old.")

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old." .format(first_name, last_name, age))

# first_name ="Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old." .format(age, last_name, first_name)) #this will print the order I typed the .format

# hw = "Hello %s" % "world"
# py = "I love Python %d" % 3
# print(hw,py)

string = "hello world"
print(string.upper())




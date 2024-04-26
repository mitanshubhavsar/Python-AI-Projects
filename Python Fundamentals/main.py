#print("Hello Mitanshu")
#print('*' * 10)
#print("*" * 10)

# price = 10
# price = 20
# rating = 4.9
# name = "mitanshu"
# is_published = False
# print(price)
# print(rating)
# print(name)
# print(is_published)

# full_name = 'John Smith'
# age = 20
# is_newpatient = False

# name = input('What is your name? ')
# print('hi ' + name)

# name = input('What is your name? ')
# colour = input('What is your favourite colour? ')
# print(name + ' likes ' + colour)

# birth_year = input('Enter your BirthYear: ')
# print(type(birth_year))
# age = 2024 - int(birth_year)
# print(type(age))
# print(age)

# pounds = input("Enter the weights in pounds: ")
# in_kg = float(pounds) / 2.205
# print(in_kg)

# course = "Python's Course for Beginners"
# print(course)
#
# courses = 'Python for "Beginners"'
# print(courses)

# course = '''
# Hi John,
#
# Here is our first email to you.
#
# Thank you,
# The support team
#
# '''
# print(course)

#course = 'Python for Beginners'
# print(course[0])
# print(course[-1])
# print(course[-2])
#print(course[0:3])
# print(course[1:])
# print(course[:4])
# print(course[:])

# name = 'Jennifer'
# print(name[1:-1])

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course)
# print(course.find('P'))
# print(course.find('o'))
# print(course.find('Beginners'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course.replace('P', 'J'))
# print(course.replace('n', 'w'))
# print('python' in course)
# print('Python' in course)

# x = 10
# x = x + 3
# x += 3
# print(x)
# x = 10 + 3 * 2 ** 2
# print(x)
# x = (10 + 3) * 2 ** 2
# print(x)

# x = 2.6
# print(round(x))
# print(abs(-2.9))
# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))

# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It is lovely day")
# print("Enjoy your day")

# price = 10 ** 6
# has_goodcredit = False
# if has_goodcredit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down Payment: ${down_payment}")

# has_high_income = False
# has_good_credit = True
# has_criminal_record = False
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# if has_high_income or has_good_credit:
#     print("Eligible for loan")
# if has_high_income or not has_criminal_record:
#     print("Eligible for loan")

# temperature = 35
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# name = "John smith"
# if len(name) < 3:
#     print("Name must be at least 3 characters.")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters.")
# else:
#     print("Name looks good!")

# weight = float(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     print(f'You are {weight*0.4536} kilos')
# elif unit.upper() == "K" or unit == "k":
#     print(f'You are {weight/0.4536} pounds')
# else:
#     print('Invalid Choice')

# i = 1
# while i<=5:
#     print("*" * i)
#     i = i + 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     val = int(input("Guess: "))
#     guess_count += 1
#     if secret_number == val:
#         print("You Win!")
#         break
# else:
#     print("Sorry, you failed!")

# command = input(">")
# if command.upper() == "HELP":
#     print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#
#     command = input(">")
#     while command != "QUIT":
#         if command.upper() == "START":
#             print("Car started...Ready to go!")
#         elif command.upper() == "STOP":
#             print("Car stopped.")
#         elif command.upper() == "QUIT":
#             break
#         else:
#             print("I don't understand that...")
#         command = input(">")
# else:
#     print("I don't understand that...")

# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped...")
#     elif command == "help":
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that...")

# for item in 'Python':
#     print(item)

# for item in ['Mosh', 'John', 'Rahul']:
#     print(item)

# for item in [1,2,3,4,5,6,7,8]:
#     print(item)

# for item in range(10):  0 to 9
#     print(item)

# for item in range(5,10):  5 to 9
#     print(item)

# for item in range(0,11,2):  0 to 10 skipping 2 no.s
#     print(item)

# total_cost = 0
# prices = [10,20,30]
# for price in prices:
#     total_cost = total_cost + price
# print(f"Total: {total_cost}")

# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     print("x" * item)

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# names = ['John','Bob','Mosh','Seema','Mary']
# print(names)
# print(names[0])
# print(names[-1])
# print(names[-2])
# print(names[2:])
# print(names[2:4])
# print(names[:])
# names[0] = 'Joh'
# print(names)

# my_list = [4, 1, 6, 10, 5, 11]
# largest = my_list[0]
# for item in my_list:
#     if item > largest:
#         largest = item
# print(largest)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][1])
# matrix[0][1] = 20
# print(matrix[0][1])
#
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5, 2, 1, 1, 7, 4]
# numbers.append(20)
# numbers.insert(0,10)
# numbers.remove(7)
# numbers.pop(5)
# print(numbers)
# print(numbers.index(10))
# print(10 in numbers)
# print(69 in numbers)
# print(numbers.count(1))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# numbers.clear()
# print(numbers)
# print(numbers2)

# numbers = [2, 6, 9, 2, 9, 10, 4, 11]
# for item in numbers:
#     if numbers.count(item) > 1:
#         for k in range(numbers.count(item) - 1):
#             numbers.remove(item)
#
# print(numbers)

# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# numbers = (1, 2, 3)
# numbers[0] = 10 we cannot modify tuples
# print(numbers[0])

# coordinates = (1, 2, 3) for tuples
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#
# x, y, z = coordinates     this is called unpacking

# coordinates = [1, 20, 3]
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# print(customer["name"])
# print(customer.get("name"))
# print(customer.get("birthdate")) return none not give error
# print(customer.get("Birthdate", "Jan 1 1980")) gives default value mentioned
# customer["name"] = "jack Smith"
# print(customer["name"])

# num_words = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
# }
# number = input("Phone: ")
# in_words = ""
# for digit in number:
#     in_words = in_words + num_words[digit] + " "
# print(in_words)

# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
#
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

# message  = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "🙂",
#     ":(": "☹️"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# def greet_user():
#     print("Hi there!")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user()
# print("Finish")

# def greet_user(name):  name is parameter here
#     print(f'Hi {name}')
#     print("Welcome Aboard")
#
#
# print("Start")
# greet_user("Jack")
# greet_user("Mary")  Mary is argument here
# print("Finish")

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print("Welcome Aboard")
#
#
# print("Start")
# # greet_user("Jack", "Smith") these are positional arguments there order matters
# print("Finish")
#
# greet_user(last_name="Jack", first_name="Smith")  these are keyword arguments here the order does not matter
# calc_cost(total=50, shipping=5, discount=0.1)

# def square(number):
#     return number * number
#
#
# def square1(number):
#     print(number * number)
#
#
# result = square(3)
# print(result)
# print(square(3))
# print(square1(3))

# def word_emoji(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "🙂",
#         ":(": "☹️"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(word_emoji(message))

# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

# Numbers
# Strings
# Booleans
# ---
# Lists
# Dictionaries
# numbers = [1, 2, 3]
# point.get_distance() methods

# class Point:
#     def move(self):  inintialising the constructor
#         print("move")
#
#     def draw(self):
#
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)


# class Point:
#     def __init__(self, x, y):  #constructor used to create or construct object
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point = Point(10, 20)
# point.x = 11
# print(point.x)


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'Hi I am {self.name}')
#
# Sam = Person("sam Hero")
# Sam.talk()
# print(Sam.name)
# Bob = Person("Bob Smith")
# Bob.talk()

# class Dog:
#     def walk(self):
#         print("walk")
#
#
# class Cat:
#     def walk(self):       here we have repeated the
#         print("walk")     walk method again instead use inheritance

# class Mammal:
#     def walk(self):
#         print("walk")

# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
# class Cat(Mammal):
#     pass
#
# class Fox(Mammal):
#     def be_annoying(self):
#         print("annoying")
#
# dog1 = Dog()
# dog1.walk()
# dog1.bark()
# fox1 = Fox()
# fox1.be_annoying()

# import converters
# print(converters.kg_to_lbs(70))
#
# from converters import lbs_to_kg
# print(lbs_to_kg(12))

# from utils import find_max
# print(find_max([4, 1, 6, 10, 5, 11]))

# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping, calc_tax
# calc_shipping()
# calc_tax()

# from ecommerce import shipping
# shipping.calc_shipping()
# shipping.calc_tax()

# import random
#
# for i in range(3):
#     print(random.random())
#
# for i in range(3):
#     print(random.randint(10, 20))  #gives random values from 10 to 20
#
# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)

import random

# class Dice:
#     def roll(self):
#         face1 = random.randint(1,6)
#         face2 = random.randint(1,6)
#         faces = (face1, face2)
#         return faces
#
# dice1 = Dice()
# print(dice1.roll())


# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first,second
#
#
# dice = Dice()
# print(dice.roll())

# Two Types of Path
#Absolute Path  ex. c:\Program Files\Microsoft
#Relative Path

from pathlib import Path
# path = Path("ecommerce")
# path1 = Path("emails")
# print(path.exists())
# print(path1.exists())

# print(path1.mkdir())
# print(path1.rmdir())

# path = Path()
# for file in path.glob('*.py'):   shows all py extension files
#     print(file)                  in current directory

# for file in path.glob('*'):   #shows all files
#      print(file)


# #1. print Hello World
# print( "Hello World")
# #2. print "Hello Noelle!" with the name in the variable
# name = "Noelle"
# print( "Hello", name)
# print("Hello "+name)

# name = 42
# print("Hello", name)
# print("Hello"+ str(name))

# food_one = "croissant"
# food_two = "bagel"
# print("I love to eat", food_one, "and", food_two)
# print(f'I love to eat {{food_one}} and {{food_two}}')

def say_hello(name):
    if name:
        print "Hello, " + name + 'from inside the function'
    else:
        print 'No name'
print 'Outside of the function'

# ---------------------------------- Strings --------------------------------- #

print "this is a sample string"

name ="Zen"
print "My name is", name

print "My name is " + name

first_name = "Hannah"
last_name = "Mulligan"
print "My name is {} {}".format(first_name, last_name)
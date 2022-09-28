# Formatted strings

name = "Johnny"
age = 55


# Instead of doing this I can use a formatted string
# print('hi ' + name + '. You are ' + str(age) + ' years old')

# by using the f keyword in front of the string 
# this will also convert other type like int to string automatically
# This reminds me of JS template literals

print(f'hi {name}. You are {age} years old')

# Old method in python2
# I can change order by putting the order number in {}

print('hi {}, you are {} years old'.format(name, age))
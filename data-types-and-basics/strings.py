# Strings

username = 'Bear'
print(type(username))

long_string = '''
WoW
0 = 0
___
'''

print(long_string)

# concatenation

lastname = 'Grizzly'
fullname = lastname + ' ' + username
print(fullname)

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

#String indexes

stringr = "this is an example"

# I can use an index to select a specific part of the string
print(stringr[0])

# [start:stop]
print(stringr[0:5])

# [start:stop:stepover] - Stepover adds an option to skip characters between start and stop
numbers = '0123456789'
print(numbers[0:10:3])

# [start:(null)] - Selects all from specified start to the end
print(numbers[2:])

# [(null):stop] - Same as above but ends on specified line
print(numbers[:5])

# [(null):(null):stepover] - Selects whole string except the skipped over parts
print(numbers[::2])

# Negative index reverses the order of selection
new_nums = "0123"
# For example the indexes are assigned A and B to differentiate
# A = 0 1 2 3 can also be read as, B = -4, -3, -2, -1
# In this example A 0 is the same as B -4 and B -1 is same as A 3
print(new_nums[-4])

# When negative index is used with stepover it can print out reversed string
print(new_nums[::-1])
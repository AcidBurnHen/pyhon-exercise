# Dictionary 
# Data type but also a data structure
# Unlike list it has key - value pairs, it's the same as Objects in Javascript

example = {
    "a": [1, 2, 3],
    "b": "Hello there",
    "c": True
}

# Keys - Can be any data type that is immutable, has to be unique

example2 = {
    123: [1, 2, 3],
    True: "Hello there",
    None: False
}

# I can assign a second value to get, which will be the default value if
# the first value doesn't exist in the dictionary as a key
example2.get("age", 12)

# Alternative to create a dictionary
example3 = dict(name='john')
print(example3.get("name"))
print("name" in example3)

# Only checks the keys , can also be used with values
print("a" in example.keys())

# I can also use dict.items() which can return a tuple

# dict.clear() - clears the whole dictionary

# dict.copy() - copies the whole dictionary 

# dict.pop() - pops off a value and returns it
new_example = example.pop("a")
print(new_example) # returns the popped off item
print(example) # prints without the popped item
# dict.popitem() - removes a random item, practically useless

# dict.update() - updates an existing key's value, if the key is non-existent it will create a new key with the value
example.update({'age': 55})

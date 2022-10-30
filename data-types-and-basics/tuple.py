# Tuple
# Is like an immutable list

example_tuple = (1,2,3,4,5, 2)
# print(example_tuple[2])
# print(2 in example_tuple)

# Tuples can aslo be used as keys in a dictionary
example = {
    (1,2): 1
}

# Simple ways to manipulate and extract tuple data
new_tuple = example_tuple[1:3]
# print(new_tuple)

x,y,z, *o = (1,2,3,4,5,6,7)

# print(x,y,"o:", o)

# Counts number of occurences of a value in a tuple
print(example_tuple.count(2))

# Shows index of first occurence in a tuple
print(example_tuple.index(2))
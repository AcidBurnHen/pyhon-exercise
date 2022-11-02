# Set is an unoredered collection of unique items
# It's similar to dictionary but it doesn't have key - value pairs

example_set = {1,2,3,4,5, 5, 5}
# Prints only one 5 value because of the unique restraint 
print(example_set)

example_set.add(100)
example_set.add(2)

example_list = [1, 1, 2, 2, 3, 3]
set_list = set(example_list)
print(set_list)

# Set's do not support indexing
# print(set_list[1]) Throws error

print(1 in set_list) # true

reverse_list = list(set_list)
print(reverse_list)

# copy()
new_set = example_set.copy()
print("NEW SET:_", new_set)

# clear()
example_set.clear()
print(example_set)

print("________________________________")
print("                                ")
first_set = {0, 1, 2, 3, 4, 5, 6}
second_set = {5, 6, 7, 8, 9, 4}

# difference()
# Finds the difference of the first set compared to the second_set
print("Difference:", first_set.difference(second_set))

# discard()
# Discards the value that is in set
#first_set.discard(4)
# print("Discard", first_set)

# difference_update()
# Removes all values from first_set that overlap with second_set values
# first_set.difference_update(second_set)
# print("Difference_update:", first_set)

# intersection()
# Returns the duplicate values found in both first_set and second_set
print(first_set.intersection(second_set))


# isdisjoint()
# Returns true if the first_set doesn't have same values as second_sets
print(first_set.isdisjoint(second_set))

# issubset()
# Returns true if all first_set values are located in second_set
first_set = {4,5}
print(first_set.issubset(second_set))

# issuperset()
# Returns ture if the first_set values encompass the second_set values, reverse of subset
print(first_set.issuperset(second_set)) # prints false

# union()
# Joins two sets together and removes duplicates 
print(first_set.union(second_set))
# There is a shorthand in for using a union between sets with a pipe
print(first_set | second_set)
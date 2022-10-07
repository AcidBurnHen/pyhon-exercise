# Lists - like arrays from JS

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd']
li3 = [1, 2, 'a', True]

# Slicing 
shopping_cart = [
    'notebooks', 
    'icecream',
    "GTA V",
    "grapes",
    "sunglasses",
    "pineapple pizza"
    ]

# Same as in string, I can use [start:stop:stepover] to slice a list 
# print(shopping_cart[0::2])

# Lists are mutable, meaning I can change the items in them directly
shopping_cart[0] = "pencil"
print(shopping_cart)

new_cart = shopping_cart
# Changing new cart changes the old shoppign cart because when new cart is assigned
# it does not copy the list, but only references what is already in memory

# The workaround is to assign the new variable to a full copied list like:
new_cart = shopping_cart[:] 
new_cart[0] = "shower gel"

print(f"new: {new_cart}", f"old: {shopping_cart}")

# Matrix
# A way to describe multi-dimensional lists

matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]

print(matrix[0][1])

# List methods

basket = ["apple", "banana", "milka", "icecream"]

# Adding to list

# Adds at end of list
basket.append("cookies")

# Adds to specific place in list
basket.insert(0, "macbook")

# Extends the list with another list
basket.extend(["pear", "pineapple"])


# Removing from list 

# Removes item from specific index, defaults to last, also returns the removed value
basket.pop()

# Removes specific value 
basket.remove("apple")

# Completely clears the list
# basket.clear()

# Finds index of specific value
basket.index("banana") 

# Shows how many times a value occurs in a list
basket.count("milka")

# Sorts the list in asc or desc order, doesn't return anything, modifies original
basket.sort()

# Returns a new sorted list
new_basket = sorted(basket)

# Copies the list
basket.copy()

# Reverses the list order 
basket.reverse()

print(new_basket)
print(basket)

new_list = list(range(101))

print(new_list)

# Combining a list into a string
sentence = ' '.join(['hi', 'my', 'name', 'is', 'bear'])

print(sentence)

# List unpacking

a,b,c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a, b, c, other, d)
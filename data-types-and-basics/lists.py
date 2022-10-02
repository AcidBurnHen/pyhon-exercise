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
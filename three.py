x = [23, 'Python', 23.98]

# Printing the original list
print(x)

# Creating a new list containing the types of elements in the original list
types_list = [type(element) for element in x]

# Printing the list of types
print(types_list)

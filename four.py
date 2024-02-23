def unique_list(input_list):
  # Using set to get unique elements and converting it back to list
  unique_items = list(set(input_list))
  return unique_items

# Sample List
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

# Calling the function
result = unique_list(sample_list)

# Printing the result
print("Sample List:", sample_list)
print("Unique List:", result)

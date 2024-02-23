def count_upper_lower(input_string):
  # Initializing counters
  upper_count = 0
  lower_count = 0

  # Iterating through each character in the string
  for char in input_string:
      # Checking if the character is an uppercase letter
      if char.isupper():
          upper_count += 1
      # Checking if the character is a lowercase letter
      elif char.islower():
          lower_count += 1

  # Printing the results
  print("No. of Upper-case characters:", upper_count)
  print("No. of Lower-case characters:", lower_count)

# Input String
input_string = 'The quick Brow Fox'

# Calling the function
count_upper_lower(input_string)

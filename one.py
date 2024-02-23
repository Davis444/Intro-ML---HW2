# Initialize the star count
stars = 1

# Loop to print stars in ascending order
for i in range(5):
    print('* ' * stars)
    stars += 1

# Reset the star count for descending order
stars = 4

# Loop to print stars in descending order
for i in range(4):
    print('* ' * stars)
    stars -= 1

# Example list
my_list = [1, 2, 3, 4, 5]

# Number of times to cycle through the list
cycles = 3

# Initialize the starting index
index = 0

# Create a list of sublists
sublists = []

# Iterate through the list with a step of 2
for _ in range(cycles):
    sublist = []
    for _ in range(len(my_list)):
        sublist.append(my_list[index])
        index = (index + 1) % len(my_list)  # Increase index by 1 to get every other element
    sublists.append(sublist)

# Print the sublists
for sublist in sublists:
    print(*sublist)

import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]
    #infile gives the opened file the temporary name infile 
    # indicated that we read the file

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
number = int(input("How many names do you want: "))
chosen_names = random.sample(names, number)

# Display the chosen names, one per line
for name in chosen_names:
    print(name)

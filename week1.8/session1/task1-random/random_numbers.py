import random

# Get user to input how many random numbers they want
numbers = int(input("How many random numbers they want: "))
# Generate this many random numbers

#we need to open the file first
with open ("random.txt", "w")as outfile:
for i in range(numbers):
    random_numbers = random.randint(1, 100)


# Write the random numbers to a file named random.txt, one number per line
    outfile.write(str(random_numbers) + "/n")
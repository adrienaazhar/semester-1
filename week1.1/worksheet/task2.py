"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
try:
    amount = int(input("Enter the amount to save every month: ")) 
# must be indented
# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
    total = amount * 12
# print this out for the user with a suitable message.
    print(f"The amount of money by the end of the year is (12 months): {total}")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
    finalamount = (total * 0.008) + total
# print this out in the format £X.XX (to two decimal places).
    print(f"The total amount of money by the end of the year is (including interest): £{finalamount:.2f}")

# Validate that they have entered an integer.
except:
    print("Invalid amount! The amount must be integers only.")
# printf can be used to tell the python that{name} should be replaced by the variable's value.


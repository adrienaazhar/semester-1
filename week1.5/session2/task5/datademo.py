# Week 1.5, Session 2: Task 5
from data import Dataset
# Write a program here to create a Dataset containing data
# from a file named by the user
filename = input("Enter a filename: ")
# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)
dataset = Dataset(filename)
print("Dataset size: ", len(dataset))
print("Dataset mean: ", dataset.mean())
print("Dataset median: ", dataset.median())

for value in dataset:
    print(value)
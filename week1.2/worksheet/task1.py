# Worksheet 1.2: Task 1 Solution

# Ask the users enter their grade
# to evaluate use try except
import sys 
try:
   grade =int(input("Enter your grade (0-100): "))

except ValueError :
     sys.exit("Error: Grade must be an integer between 0 and 100")
    
if grade < 0 or grade > 100 :
     sys.exit("Error: Grade must be an integer between 0 and 100")

# Converts that grade into a result of Pass, Fail or Distinction- Fail = 0-39 - Pass = 40-69 - Distinction = 70-100

if grade >= 0 and grade <=39 :
    print(f"{grade} is a Fail")
elif grade >= 40 and grade <= 69 :
    print(f"{grade} is a Pass")
else :
    print(f"{grade} is a Distinction")


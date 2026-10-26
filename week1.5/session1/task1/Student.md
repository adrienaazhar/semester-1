# Student Class
class Student: 
## Attributes (state)
    def __init__(student, name, age, ID, course):
        student.name = name
        student.age = age
        student.ID = ID
        student.course = course
    

## Behaviour (methods)
    def study(student):
        print(student.name, "is studying.")

    def classes(student):
        print(student.name, "is studying computer science.")

    def display_information(student):
        print("Name:", student.name)
        print("Age:", student.age)
        print("Student ID:", student.ID)
        
#Create a student
s1 = Student("Adriena", 19, 2025461396, "Computer Science")

#call the behaviour
s1.study()
s1.classes()
s1.display_information()


# Student Class
class Student: 
## Attributes (state)
    def __init__(self, name, age, ID, course):
        self.name = name
        self.age = age
        self.ID = ID
        self.course = course
    

## Behaviour (methods)
    def study(self):
        print(self.name, "is studying.")

    def classes(self):
        print(self.name, "is studying computer science.")

    def display_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.ID)
        
#Create a student
s1 = Student("Adriena", 19, 2025461396, "Computer Science")

#call the behaviour
s1.study()
s1.classes()
s1.display_information()


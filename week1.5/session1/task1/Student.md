# Student Class
class Student: 
## Attributes (state)
    def student_attributes(student, name, age, ID, course):
        student.name = "Adriena"
        student.age = 19
        student.ID = 202923514
        student.course = "Computer Science"
    

## Behaviour (methods)
    def study(student):
        print(student.name, "is studying.")

    def classes(student):
        print(student.name, "is studying computer science.")

    def display_information(student):
        print("Name:", student.name)
        print("Age:", student.age)
        print()

# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Point, Circle

circle = Circle(5)

point1 = Point(3,2)
point2 = Point(7,3)

print(point1 in circle)
print(point2 in circle)
# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """
    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point with a given x and y coordinates.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # Add distance() method here
    def distance(self):
        """
        Returns distance from this Point to origin.
        """
        return math.hypot(self.x_coordinate, self.y_coordinate)

    # Add distance_to() method here
    def distance_to(self, other):
    # (This will need a parameter representing another point)
        """
        Returns the distance from this POint to another.
        """
        return math.hypot(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate
    )

# Finally, add code here to demonstrate use of Point
p1 = Point(3,4)

print("X coordinate: ", p1.x_coordinate)
print("Y coordinate: ", p1.y_coordinate)
print("Distance from origin: ", p1.distance())

p2 = Point(6,9)

print("Distance between points: ", math.hypot(p1.distance_to(p2)))


# Add a definition for a Circle class here, giving it
class Circle:
    """
    A Circle that has radius and centre.
    """
    def __init__(self, radius, centre)
    - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
        """
        Creates a Circle with a given radius and centre.
        """
        self.radius = radius
        self.centre = centre

#  
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!

# Week 1.5, Session 1: Task 3
import math

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


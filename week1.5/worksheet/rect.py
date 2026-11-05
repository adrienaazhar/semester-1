# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")

        if not isinstance(height, int):
            raise TypeError("Height must be an integer")

        if width <=0 or height <=0:
            raise ValueError("Width and height must be positive")

        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """
        Check and return whether the rectangle is a square.
        """
        return self.width == self.height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle
        """
        return (self.width + self.height) * 2
 # (See README.md for details of what they should do)
# Demo program

rectangle1 = Rectangle(9,9)

print(rectangle1.is_square())
print(rectangle1.area())
print(rectangle1.perimeter())
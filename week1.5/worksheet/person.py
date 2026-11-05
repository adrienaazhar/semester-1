# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
        """
        Creates a person with a name and date of birth.
        """
    

        if not isinstance(name,str):
            raise TypeError("Name must be a string")

        if name =="":
            raise ValueError("Name must not be empty")

        if not isinstance(birth, date):
            raise TypeError("Birth must be a date")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here

    def initials(self):
        """
        Return the uppercase initials of the person's name.
        """
        words = self.name.split()
        letters = ""

        for word in words:
            letters = letters + word[0].upper()

        return letters
    
    def is_birthday(self):
        """
        Check whether the person's birthday is today.
        """
        today = date.today()

        return today.month == self.birth.month and today.day == self.birth.day
    # (see README.md for further details)

    #Demo program

person1 = Person("Adriena Binti Azhar", date(2007, 8, 1))

print(person1.initials())
print(person1.is_birthday())

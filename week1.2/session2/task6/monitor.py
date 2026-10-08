# Week 1.2, Session 2: Task 6

temperature =int(input("The machine's temperature in degrees Celsius (integer): "))
pressure =int(input("The machine's pressure in PSI (integer): "))
operational =int(input("The machine's operational status (1 for operating, 0 for stopped) (integer): "))

#operating conditions

if (temperature >80):
    print("The temperature is too high. Recommend shutting down the machines")

elif
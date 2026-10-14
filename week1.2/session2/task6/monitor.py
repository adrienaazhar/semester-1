# Week 1.2, Session 2: Task 6

temperature =int(input("The machine's temperature in degrees Celsius (integer): "))
pressure =int(input("The machine's pressure in PSI (integer): "))
operational =int(input("The machine's operational status (1 for operating, 0 for stopped) (integer): "))

#operating conditions

#temperature
if temperature >80:
    print("The temperature is too high. Recommend shutting down the machines")

elif temperature>=50 and temperature<=80 :
    print("The temperature is within safe limits")

else:
    print("The machine temperature is low and no action is needed") 

#pressure
if pressure >100 :
    print("Alert that high pressure is detected and maintainance is needed")

elif pressure >= 70 and pressure <=100 :
    print("Pressure is stable")

else :
    print("The pressure is low and the system is operating normally")

#Determine status
if temperature >80 or pressure >100 :
    print("The machines is running in unsafe conditions and recommend shutting it down")

elif (temperature>=50 and temperature<=80) or (pressure >= 70 and pressure <=100):
    print("The machines is running normally")

else:
    print("The machines is stopped and no actions is needed")
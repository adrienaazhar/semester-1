"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Nur Syafeera Adriena Binti Azhar
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  
# read an integer number of steps (>0)

state = "red"
state_time = 0

# Simulate the traffic light system up to time=maxtime in 1-second steps

# systime starts with 0 while maxtime must be greater than 0
while systime <= maxtime :
    print(f"Time {systime:03} State {state}")
# Print the output that the user input then the system must be add 1 to make sure the program keep running
    systime = systime + 1
    state_time = state_time + 1
#
    if state_time == states [state]:
        if state == "red":
            state = "red_amber"

        elif state == "red_amber":
            state = "green"

        elif state == "green":
            state = "amber"

        elif state == "amber":
            state = "red"

        state_time = 0

        
# At the end of each step you should output the time and state using the statement on line 14
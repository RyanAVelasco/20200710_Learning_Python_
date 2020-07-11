# NOTE: I'm very familiar with this level of python so this was solved before I read the chapter.


# Question 2: Write a program that uses input to prompt a user for name and then welcomes them.
# Enter your name: Chuck  <= Input
# Hello Chuck  <= Output
name = input("Please enter your name: ")
print("Hello " + name)


# Question 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
# We won’t worry about making sure our pay has exactly two digits after the decimal place for now. If you want,
# you can play with the built-in Python round function to properly round the resulting pay to two decimal places.
hours = float(input("Please enter hours worked: "))
rate = float(input("Please enter pay per hour: "))
pay = hours * rate
print(pay)

print(hours * rate)  # Alternative and shorter way of solving the exercise


# Question 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
# For each of the following expressions, write the value of the expression and the type
# (of the value of the expression).
# (1) width//2
# (2) width/2.0
# (3) height/3
# (4) 1 + 2 * 5
# Use the Python interpreter to check your answers.
print(width // 2)  #  8, integer
print(width / 2.0)  #  8.5, float
print(height / 3)  #  4.0, float
print(1 + 2 * 5)  #  11, integer

# Question 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
# and print out the converted temperature.
celsius = int(input("What is the current temperature in Celsius? "))
fahrenheit = (celsius * 1.8) + 32  # formula: (C * 1.8) + 32 = F
print(fahrenheit)
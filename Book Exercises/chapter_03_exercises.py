# NOTE: Question 2 is the only concept I'm unfamiliar with (try/except)


# Question 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked
# above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
hours = 45
rate = 10
if hours > 40:
    print(rate * 1.5 * hours)
else:
    print(rate * hours)  #  <= 40 would return max: 400


# Question 2: Rewrite your pay program using try and except so that your program handles non-numeric input
# gracefully by printing a message and exiting the program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input


# Question 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
# print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
#
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for input.

while True:
    score = input("Enter Score: ")
    if score <= 1.0 and score > 0.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")
    elif score is not float(score) or score > 1.0:
        print("Bad score")

# I'm having trouble with the program outputting 'Bad score' when I enter 'perfect' because what I input is
# converted to a float. I tried adding try to the if/elif statements but I come upon the problem of every input
# showing ouput 'Bad score'.
# I next tried this line:
#   elif score is not float(score) or score > 1.0:  Failed

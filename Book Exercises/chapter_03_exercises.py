print("NOTE: Question 2 is the only concept I'm unfamiliar with (try/except)\n")


print("""\n\n=== Question 1 ===
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worke
above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0""")
print("\n== Answer ==")
hours = 45
rate = 10
if hours > 40:
    print(rate * 1.5 * hours)
else:
    print(rate * hours)  #  <= 40 would return max: 400


print("""\n\n=== Question 2 ===
Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by 
printing a message and exiting the program. The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input""")
print("\n== Answer ==" + " Part A ==")
hours = 45
rate = "nine"
try:
    if hours > 40:
        print(rate * 1.5 * hours)
    else:
        print(rate * hours)  #  <= 40 would return max: 400
except:
	print("Error, please enter numeric input")

print("\n== Answer ==" + " Part B ==")
hours = "forty"
rate = 9
try:
    if hours > 40:
        print(rate * 1.5 * hours)
    else:
        print(rate * hours)  #  <= 40 would return max: 400
except:
	print("Error, please enter numeric input")


print("""\n\n=== Question 3 ===
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range print an error message.
If the score is between 0.0 and 1.0, print a grade using the following table:
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly as shown above to test the various different values for input.""")

print("\n=== Answer === This is the initial code answering the question within the parameters of the question ==")
score = input("Enter Score: ")
try:
    score = float(score)  # Is there a more efficient way to do this?
    if score > 0.0 and score < 1.0:
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
    else:
        print("Bad score")
except:
    print("Bad score")

# I'm having trouble with the program outputting 'Bad score' when I enter 'perfect' because what I input is
# converted to a float. I tried adding try to the if/elif statements but I come upon the problem of every input
# showing output 'Bad score'.
# I next tried this line:
#   elif score is not float(score) or score > 1.0:  Failed
# So I found the solution which was to use try, convert to float in that statement and use except to handle any strings
# that would be inputted.  I'm sure there must be a more efficient way of doing this.'
# I wanted to make the code automatically enter the required values for the exercise so I coded a loop below updating
# a 'n' variable for each iteration

print("\n=== Answer === This is my automatic code solving the solution ==")
count = 0
n = 0
while count < 5:  # these are the values told to input to test the code
    if count == 0:
        n = "0.95"  # answer should be A
    elif count == 1:
        n = "perfect"  # answer should be Bad Score
    elif count == 2:
        n = "10.0"  # answer should be Bad Score
    elif count == 3:
        n = "0.75"  # answer should be C
    elif count == 4:
        n = "0.5"  # answer should be F

    score = n

    try:
        score = float(n)
        if score > 0.0 and score < 1.0:
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
        else:
            print("Bad score")
    except:
        print("Bad score")

    count += 1

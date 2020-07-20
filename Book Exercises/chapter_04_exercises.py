import random

print("""\n\n=== Exercise 1 ===
Run the program on your system and see what numbers you get. Run the program more than once
and see what numbers you get.

import random
for i in range(10):
    x = random.random()
    print(x)""")

print("""\n=== Answer ===
'I've modified to code a bit to include lists to make it easier to see the difference.'""")
numList1 = []  # Run 1 list
numList2 = []  # Run 2 list
numList3 = []  # Run 3 list

for i in range(10):
    x = random.random()
    numList1.append(x)

for i in range(10):
    x = random.random()
    numList2.append(x)

for i in range(10):
    x = random.random()
    numList3.append(x)

print("Run One:\n", numList1)
print("Run Two:\n", numList2)
print("Run Three:\n", numList3)


print("""\n\n=== Exercise 2 ===
Move the last line of this program to the top, so the function call appears before the definitions. 
Run the program and see what error message you get.

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()""")

print("""\n=== Answer ===
'Added a try exception to make sure the entire program runs'""")
try:
    repeat_lyrics()
except:
    print("When the function call is moved above the definitions it returns: NameError")


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


print("""\n\n=== Exercise 3 ===
Move the function (same as above) call back to the bottom and move the definition of print_lyrics 
after the definition of repeat_lyrics. What happens when you run this program?""")

print("""\n=== Answer ===""")


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

print("When the code is run after moving the definition nothing changes in the output.")


print("""\n\n=== Exercise 4 ===
What is the purpose of the 'def' keyword in Python?

a) It is slang that means 'the following code is really cool'
b) It indicates the start of a function
c) It indicates that the following indented section of code is to be stored for later
d) b and c are both true
e) None of the above""")

print("""\n=== Answer ===
d: b and c are both true""")

print("""\n\n=== Exercise 5 ===
What will the following Python program print out?

def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()

a) Zap ABC jane fred jane
b) Zap ABC Zap
c) ABC Zap jane
d) ABC Zap ABC
e) Zap Zap Zap""")

print("""\n=== Answer ===
d) ABC Zap ABC""")

print("""\n\n=== Exercise 6 ===
Rewrite your pay computation with time-and-a-half for overtime and create a function called compute
pay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0""")

print("""\n=== Answer ===""")
h = 45
r = 10


def compute(hours, rate):
    print(h * r, "<-- Does not include time-and-a-half overtime")
    print(h * (r * 1.5), "<-- Includes time-and-a-half overtime")


compute(h, r)

print("""\n\n=== Exercise 7 ===
Rewrite the grade program from the previous chapter using a function called compute 
grade that takes a score as its parameter and returns a grade as a string. 

Score Grade
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
Run the program repeatedly to test the various different values for input.""")

print("""\n=== Answer ===""")


def compute(score):
    try:
        score = float(score)  # Is there a more efficient way to do this?
        if 0.0 < score < 1.0:  # This was not taught in chapter, it was a test I thought of which worked!
            if score >= 0.9:
                return "A"
            elif score >= 0.8:
                return "B"
            elif score >= 0.7:
                return "C"
            elif score >= 0.6:
                return "D"
            elif score < 0.6:
                return "F"
        else:
            return "Bad score"
    except:
        return "Bad score"


score = input("Enter score: ")	    
print(compute(score))

print("\n=== Answer === This is my automatic code solving the solution ==")

count = 0
n = 0


def compute2(score):
    try:
        score = float(score)  # Is there a more efficient way to do this?
        if 0.0 < score < 1.0:
            if score >= 0.9:
                return "A"
            elif score >= 0.8:
                return "B"
            elif score >= 0.7:
                return "C"
            elif score >= 0.6:
                return "D"
            elif score < 0.6:
                return "F"
        else:
            return "Bad score"
    except:
        return "Bad score"


while count < 5:  # these are the values told to input to test the code
    if count == 0:
        print(compute2(score="0.95"))  # answer should be A "I tried out adding an expression to print! It worked!"
    elif count == 1:
        print(compute2(score="perfect"))  # answer should be Bad Score
    elif count == 2:
        print(compute2(score="10.0"))  # answer should be Bad Score
    elif count == 3:
        print(compute2(score="0.75"))  # answer should be C
    elif count == 4:
        print(compute2(score="0.5"))  # answer should be F
    count += 1

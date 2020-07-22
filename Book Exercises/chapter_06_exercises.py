print("""

Exercise 1: Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
Another way to write a traversal is with a for loop:
    
    for char in fruit:
        print(char)
""")

print("""
=== Answer ===
I'm not sure how to stop getting IndexError with the program I wrote while
getting it work. 
""")

# index = 0
# word = "Four light novels based on The Seven Deadly Sins have been published"
# while index < len(word):
#     for ltr in word[index - 1]:
#         print(ltr)
#         index -= 1


print("""

Exercise 2:  Given that fruit is a string, what does fruit[:] mean?""")

print("""
=== Answer ===

[:] means that all characters from the start of the string to 
the end are included in the search.
""")


print("""
Exercise 3: Encapsulate this code in a function named count, and generalise 
it so that it accepts the string and the letter as arguments.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
    print(count)
""")

print("""
=== Answer ===""")


def count(word, char):
    for char in word:
        if char in word:
            count += 1



word = 'banana'
count = 0

for letter in word:
    if letter == 'a':
        count = count + 1
    print(count)

print("""

=== Exercise 5 === 
Take the following Python code that stores a string:

str = 'X-DPSAM-Confidence:0.8475'

Use find and string to extract the portion of the string after the colon
character and then use the float function to convert the extracted string
into a floating point number.""")

print("""
=== Answer ===""")

str = 'X-DPSAM-Confidence:0.8475'
atpos = str.find(":")
sppos = str.find("'", atpos)
host = str[atpos + 1:sppos]
print(float(host))

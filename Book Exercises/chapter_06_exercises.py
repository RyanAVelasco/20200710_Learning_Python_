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


print("""
=== Answer.alt ===
I'm going to use https://en.wikipedia.org/wiki/The_Seven_Deadly_Sins_(manga)#Reception
to find every occurence of 'the' and print out the the next 30 chars
""")

str = """
The 2014 edition of Kono Manga ga Sugoi!, which surveys people in the manga and publishing industry, named The Seven
Deadly Sins the fifth best manga series for male readers.[78] The title was named Best Shōnen Manga at the 39th Kodansha
Manga Awards alongside Yowamushi Pedal.[79] It was also nominated for the 2014 Manga Taishō award and as Best Youth
Comic at the 42nd Angoulême International Comics Festival in France.[80][81]

In October 2017, Netflix revealed that The Seven Deadly Sins anime was the fourth most binge-watched show within its
first 24 hours of release on their platform.[82]

Sales
As of August 2014, the collected volumes of The Seven Deadly Sins had 5 million copies in circulation.[32] By
January 2015, this number had grown to 10 million sold.[83] As of June 2018, the series has 28 million copies in
circulation,[84] and over 30 million copies in circulation as of December 2018.[85] The first collected volume of the
series sold 38,581 copies in its first week, ranking number 13 on the Oricon manga chart.[86] Its second volume ranked 5
selling 106,829 in its first week,[87] while its third debuted at number 4 with 135,164 copies.[88] The thirteenth
volume had the manga's best debut week to date, selling 442,492 for first place on the chart.[89] The series was the
ninth best-selling manga of 2014, with over 4.6 million copies sold that year.[90] For the first half of 2015, The Seven
Deadly Sins was the number one best-selling series.[91] It finished the year in second place with over 10.3 million
copies sold, behind only One Piece.[92] It was the sixth best-selling of 2016, with over 5 million copies sold, and the
seventh of 2017, with close to 3.6 million copies sold.[93][94]

The North American releases of volumes two and four charted on The New York Times Manga Best Seller list at number seven
and nine respectively.[95][96]

The first DVD volume of the anime debuted at number one on Oricon's Japanese animation DVD chart with 3,574 copies
sold.[97] With 32,762 copies sold of the five volumes released at the time, The Seven Deadly Sins was the 30th
best-selling anime of the first half of 2015.[98]

The novel The Seven Deadly Sins -Gaiden- Sekijitsu no Ōto Nanatsu no Negai was the 33rd best-selling light novel of the
first half of 2015, with 61,939 copies sold.[99]

Critical reception
Rebecca Silverman of Anime News Network (ANN) gave the first volume a B grade, calling the art interesting and the story
a 'neat take on the basic knights-in-shining-armor.' She saw influence from Akira Toriyama in Meliodas and 1970s shōjo
manga in the female characters. However, Silverman felt the art had issues with perspective and commented that Elizabeth
lacked character development.[100] Both Silverman and Danica Davidson of Otaku USA warned that Meliodas' perverted
actions towards Elizabeth, which are used for comedic relief, could possibly be misinterpreted by some readers.[100][
01] In a brief review, Jason Thompson claimed that the series follows common shōnen manga elements, making its plot
twists and dialog predictable. He did however like the art and the series' European setting.[102]

Reviewing the first anime for ANN, Theron Martin felt that the series has a slow start with generic shōnen action fare
but the storytelling picks up significantly in the second half. He had strong praise for the music and enjoyed the main
cast and their interactions, but not the common archetypal villains. Martin noted that the art has a 'semi-cartoonish
look' that one would expect in a series that 'skews a bit younger,' but The Seven Deadly Sins' graphic violence and
minimal fan service prove it's 'anything but a kiddie show.'[103]

"""

print(str)

#  clean up to remove [n]
while "[" in str and "]" in str:  #  I could use RegEx to do this but I don't want to.
    atpos = str.find("[")
    sppos = str.find("]")
    new = str[atpos - 1:sppos + 1]
    str = str.replace(new, "")

print("""
=================

""", str)
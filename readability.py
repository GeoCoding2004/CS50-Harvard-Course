# TODO
from cs50 import get_string

phrase = get_string("Type a text: ")
letters = 0

# count letters
for i in range(len(phrase)):
    if str.isspace(phrase[i]) == False:
        letters += 1

# count words
words = 1
for j in range(len(phrase)):
    if phrase[j] == " ":
        words += 1
    else:
        words = words + 0

# count sentences
sentences = 0
for k in range(len(phrase)):
    if phrase[k] == "." or phrase[k] == "!" or phrase[k] == "?":
        sentences += 1
    else:
        sentences = sentences + 0

# calculate the index and round it
index = 0.057 * ((100*letters) / words) - 0.296 * ((100*sentences) / words) - 15.8
index = round(index)

# assign the grade according to the index
if index <= 16.0 and index >= 1.0:
    print("Grade ", end="")
    print(index)
elif index < 1:
    print("Before Grade 1")
else:
    print("Grade 16+")
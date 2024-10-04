# TODO
from cs50 import get_int

# get the users input
# reprompt if int is not between 1 and 8
while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

for i in range(n):
    # loop with a range of the height - number of line - 1
    # to keep the end for the #
    for j in range(n-i-1):
        print(" ", end="")

    # loop with a range of the number of line + 1
    # because when we pass to another line, we need to add a hash to the others in the previous line
    for k in range(i+1):
        print("#", end="")
    print()


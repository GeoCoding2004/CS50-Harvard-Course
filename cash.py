# TODO
from cs50 import get_float
import math

# repromt for input until positive integer
while True:
    n = get_float("Change owed: ")
    if n > 0:
        break

# convert cents to dollars and rounding it
cash = round(n * 100)

# we divide by the categorie of change
# we take the int which means the number of change of that categorie we need
# we then substract it from the original cash to get the remaining
# and we do the same thing for each categorie of money

for i in range(25):
    k = math.floor(cash/25)
    remain = cash - (k * 25)

for j in range(10):
    k2 = k + math.floor(remain/10)
    remain1 = remain-((k2 - k)*10)

for k in range(5):
    k3 = k2 + math.floor(remain1 / 5)
    remain2 = remain1 - ((k3 - k2) * 5)

k4 = k3 + remain2
print(k4)
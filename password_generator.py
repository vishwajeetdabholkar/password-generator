import random

LOWER = "abcdefghijklmnopqrstuvwxyz"

UPPER = "ABCDEFGHJIKLMNOPQRSTUVWXYZ"

NUMBERS = "0123456789"
SYMBOLS = "[{}0*:/..-"

all = LOWER + UPPER + NUMBERS + SYMBOLS
length = 16

password = "".join(random.sample(all, length))
print(password)
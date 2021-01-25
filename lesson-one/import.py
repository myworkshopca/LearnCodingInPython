# load a module,
# a module is a package for a set of functions.
import random

# the randint function will return a number between
# the given two numbers.
# setup a index to track 
index = 0
# stop only when we got a random number equals 10,
while True:
    num = random.randint(0, 10)
    print("{0} - {1}".format(index, num))
    index += 1
    if num == 10:
        break
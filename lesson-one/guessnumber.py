import random

# show the header.
header = """
*******************************
* Welcome to Guess the Number *
*******************************
"""
print(header)

# generate the random number between 0 to 100
theNumber = random.randint(0, 100)

# inform player the range of the number.
rangeMsg = "The number is between 0 to 100"
print(rangeMsg)

# ask player to guess the number.
guessMsg = "Guess the number: "
guessNum = int(input(guessMsg))

# check the number is correct or not!
if guessNum == theNumber:
    # get ready the guess message
    awardMsg = """
%%%%%%%
% You guess the number correct!
%%%%%%%
"""
    print(awardMsg)
else:
    # get ready the guess again message.
    again = """
--------------
- You guess wrong number!
- Try again!
--------------
"""
    print(again)

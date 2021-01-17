# here is the comment
# my first ever code in Python!
print('Hello World!')

# ==============================
# how to use variable?

# define a variable is very simple:
greeting = 'The fancy greeting!'

print( greeting )

# collection user's name:
name = input( 'What is your name: ' )
print( 'Nice to meet you, ', name )

# collect user's age
age = input( "How old are you: " )

# branch out using if statement
if age <= 10:
    print( 'Sorry ', name, '! We are not allowed to provide game for kids less then 11 years old!' )
    exit()

print( 'Hi ', name, ', Welcome to the game!' )

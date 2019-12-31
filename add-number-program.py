# import string
# import random

#get the user's name
name = input('What is your name? ')
greeting = 'Hello ' + name
print(greeting)
#ask user to pick a number
number1 = int(input('Pick a number '))
print(number1)
#ask user to pick another number
number2 = int(input('Pick another number '))
print(number2)
#add both numbers together in variable called result
result = int(number1 + number2)

#Print 'The sum of' number1 '+' number2 '=' result
print('The sum of ' , number1 , '+' ,  number2 , '=' , int(result))

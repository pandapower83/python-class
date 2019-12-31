#Winchelstatecapitalsquiz.py
"""For this last assignment, you are going to make a state's capitals quiz, using a dictionary.

Create a program using Python, following the steps below:

1) Create a dictionary of US states as keys and the state capitals that correspond with your list, as the values (Choose 12 of your favorite states).

2) Then have the program quiz the user, by displaying the state's name, and asking for the capital.

                  Consider using a string manipulator to lower case, to make your comparisons easier.

3) Have the user told whether the are right or wrong, and keep track of the results in a counter (variable).

4) Once the user has completed all 12 questions, have the results printed on the screen for the user, and end the program.

 """


#import random so my print statements are random
#import random

import random

#setting my counter variables to zero
correct = 0
incorrect = 0

count = 1
#print greeting for the game
print('Welcome to the state capitals quiz! When the state is displayed, you type in the capital.')

#create my dictionary of 12 states with capitals
state_capitals = {'Texas': 'austin', 'Iowa':'des moines', 'Arizona':'phoenix', 'Arkansas':'little rock', 'Alaska':'juneau', 'Colorado':'denver','Idaho':'boise', 'Hawaii':'honolulu', 'Michigan':'lansing', 'Kansas':'topeka', 'Louisiana':'baton rouge', 'Florida':'tallahassee'}

#create a list of print statements
print_positives = ['you got it right! good job!' , 'fantastico! one point for correct!' , 'congratulations! you are on a roll' , 'like a boss!' , 'superstar!' , 'give yourself a gold star!' , ]
print_negatives = ['aww! keep studying!' , 'make flashcards for this one!' , 'better luck next time! STUDY.' , 'sorry that is incorrect!' , 'oops! you missed that one!' , 'wrong answer! that is one point for incorrect!']


again = 'y'

while again == 'y':
#less than equals to 12 because we have 12 entries in the dictionary
	while count <= 12:
#looping every key and value in my dictionary
		k , v = state_capitals.popitem()
		#counting this so we go through the dictionary 12 times
		count += 1
		#prints the key, the state
		#print(k)
		print('What is the capital of ' + k + '?')

		#ask for the capital of the state. 
		ask_capital = input()
		#make the letters of input lowercase so it matches what is in the dictionary and doesnt give an error
		ask_capital = ask_capital.lower()
		#if what the user entered is the same as the value
		if ask_capital == v:
			#correct gets 1 point
			correct += 1
			#printing randomly from my list
			print(random.choice(print_positives))
			
		else:
			#incorrect gets 1 point
			incorrect += 1
			#printing randomly from my list
			print(random.choice(print_negatives))
			
	
	print('You got ' , correct , 'correct answers and ' , incorrect, ' incorrect answers.')	
	again = input('Do you want to play again? Enter y for yes or n for no ')
	#resetting all my variables to zero so the game can be played again.  Yes this would work also with functions.
	count = 1
	correct = 0
	incorrect = 0
	state_capitals = {'Texas': 'austin', 'Iowa':'des moines', 'Arizona':'phoenix', 'Arkansas':'little rock', 'Alaska':'juneau', 'Colorado':'denver','Idaho':'boise', 'Hawaii':'honolulu', 'Michigan':'lansing', 'Kansas':'topeka', 'Louisiana':'baton rouge', 'Florida':'tallahassee'}
		
		


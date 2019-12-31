"""Have the program prompt for the players first name, and store this information.
The program should use the random module and random function.
Have the number formatted, and be between 1 and 25.
Have the user enter a guess as many times as it takes to get to the correct number, and keep track of these turns.
Have the program let the user know whether each guess was right or wrong.
Sorry, PlayerName X was incorrect.
Correct, PlayerName, X was correct
Once the correct number has been guessed, have the program report on the screen how many guesses it took the user.
Well, PlayerName, it took you X number of guesses to get the secret number.
Prompt the user to play again, and if so, have the game begin again, otherwise the program should exit.
See if / where you can integrate a function.
made by Rachel Winchel CIS 121 Spring 2018"""

import random

name = input('What is your name?')
greeting = 'Hello ' + name + ' Welcome to Guess a Number Game!' 
print(greeting)


def game():

	
	guesses = 1

	userChoice = int(input('Enter a number between 1 and 25 \n'))
	computerChoice = random.randint(1,26)
	
	while userChoice != computerChoice:
		guesses +=1
		print('Sorry', name, 'your guess of', userChoice, 'was incorrect.  Try again.') 
		userChoice = int(input('Enter a number between 1 and 25 \n'))
		if computerChoice == userChoice:
			guesses += 1
			print('Correct', name, 'your guess of', userChoice, 'was correct. Well', name, 'it took you', guesses-1, 'guesses to get the secret number.')

game()

while True:
	answer = input("Do you want to play again? Type y or n ")
	if answer == 'y':
		game()
	else:
		break
print('Have a nice day! Thanks for playing!')





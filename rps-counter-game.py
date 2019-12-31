#rock paper scissors game
#Rock beats scissors
#paper covers rock
#scissors cut paper
#program made by Rachel Winchel CIS 121 Spring 2018 RPS Version 2. Finished 3/4/18
#Contains loop so program runs 5 times
#Uses accumulators to keep track of wins, loses, ties
#Have the program validate whether the user entered a number for their Rock, Paper, or Scissors Choice.
#With an invalid entry, have the program add that to the number of ties.
#After the five games, have the program print onto the screen, the users name, and the number of wins, loses, and ties that were recorded in the game



#I imported random because I wanted to make a real game with a different result each time
import random

#get players name
name = input('What is your name?')
greeting = 'Hello ' + name
print(greeting)

#while goes here to play 5 times

gameCount = 1
wins = 0
losses = 0
ties = 0

while (gameCount <= 5):
	gameCount += 1

	#get players choice
	userChoice = int(input('Enter a number for your choice: 1. Rock 2. Paper 3. Scissors \n'))

	computerChoice = random.randint(1,3)
	 

	if (userChoice < 1 or userChoice > 3):
		ties += 1
		print("You can only enter a 1, 2, or 3. Play nice with the computer please.")

	else: 

		#determine game
		#Rock and rock tie
		if computerChoice == 1 and userChoice == 1:
			print("Well", name, "I had" , computerChoice ,  "and you had" ,  userChoice , "so we tied")
			ties = ties + 1
		#Paper covers rock. Computer choice wins
		elif computerChoice == 2 and userChoice == 1:
			print("Well", name, "I had" , computerChoice, "and you had" , userChoice, "so I won because Paper covers rock!")
			losses = losses + 1
		#Rock user choice destroys computer choice scissors.  User wins.
		elif computerChoice == 3 and userChoice == 1:
			print("Well" , name, "I had" , computerChoice, "and you had" , userChoice, "so You won because Rock breaks scissors!")
			wins = wins + 1

		#Computer choice and user choice paper is the same. Tie
		if computerChoice == 2 and userChoice == 2:
			print("Well", name, "I had" , computerChoice ,  "and you had" ,  userChoice , "so we tied")
			ties =  ties + 1
		#Paper user choice is cut by computer choice so computer won.  Scissors cut paper.
		elif computerChoice == 3 and userChoice == 2:
			print("Well", name, "I had" , computerChoice, "and you had" , userChoice, "so I won because scissors cut paper!")
			losses = losses + 1
		#computer choice rock is covered by user choice paper so user won. Paper covers rock.
		elif computerChoice == 1 and userChoice == 2:
			print("Well", name, "I had" , computerChoice, "and you had" , userChoice, "so you won because paper covers rock!")
			wins = wins + 1

		#computer choice scissors is same as user choice paper. Tie
		if computerChoice == 3 and userChoice == 3:
			print("Well", name, "I had" , computerChoice ,  "and you had" ,  userChoice , "so we tied")
			ties = ties + 1
		#user choice scissors cuts paper computer choice. User choice wins
		elif computerChoice == 2 and userChoice == 3:
			print("Well", name, "I had" , computerChoice, "and you had" , userChoice, "so you won because scissors cut paper")
			wins = wins + 1
		#computer choice rock destroys user choice scissors. Computer wins
		elif computerChoice == 1 and userChoice == 3:
			print("Well", name, "I had" , computerChoice, "and you had" , userChoice, "so I won because rock breaks scissors!")
			losses = losses + 1
		
print("Hey", name, "You won" , wins, "times and you lost" , losses , "times and you tied" , ties , "times. Awesome.")

print("See you later Alligator")

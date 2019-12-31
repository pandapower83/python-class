#rock paper scissors game
#Rock beats scissors
#paper covers rock
#scissors cut paper
#program made by Rachel Winchel CIS 121 Spring 2018

#I imported random because I wanted to make a real game with a different result each time
import random

#get players name
name = input('What is your name?')
greeting = 'Hello ' + name
print(greeting)

#get players choice
user_choice = int(input('Enter a number for your choice: 1. Rock 2. Paper 3. Scissors \n'))

#using random.randint here with the numbers in the range so computer can pick a different option each time making the game interesting
computer_choice = random.randint(1,3)
 

#determine game
#if computer choice and user choice are the same for any variation 11 22 33
if computer_choice == user_choice:
	print("Well", name, "I had" , computer_choice ,  "and you had" ,  user_choice , "so we tied")
#Paper covers rock. Computer choice wins
elif computer_choice == 2 and user_choice == 1:
	print("Well", name, "I had" , computer_choice, "and you had" , user_choice, "so I won because Paper covers rock!")
#Rock user choice destroys computer choice scissors.  User wins.
elif computer_choice == 3 and user_choice == 1:
	print("Well" , name, "I had" , computer_choice, "and you had" , user_choice, "so You won because Rock breaks scissors!")
#Paper user choice is cut by computer choice so computer won.  Scissors cut paper.
elif computer_choice == 3 and user_choice == 2:
	print("Well", name, "I had" , computer_choice, "and you had" , user_choice, "so I won because scissors cut paper!")
#computer choice rock is covered by user choice paper so user won. Paper covers rock.
elif computer_choice == 1 and user_choice == 2:
	print("Well", name, "I had" , computer_choice, "and you had" , user_choice, "so you won because paper covers rock!")
#user choice scissors cuts paper computer choice. User choice wins
elif computer_choice == 2 and user_choice == 3:
	print("Well", name, "I had" , computer_choice, "and you had" , user_choice, "so you won because scissors cut paper")
#computer choice rock destroys user choice scissors. Computer wins
elif computer_choice == 1 and user_choice == 3:
	print("Well", name, "I had" , computer_choice, "and you had" , user_choice, "so I won because rock breaks scissors!")
	

#thanks for playing 

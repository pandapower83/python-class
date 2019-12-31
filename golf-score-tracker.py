  #Golf score tracker final version 

#Winchel CIS 121 Golf Score Tracker
"""You are going to create a file to help the Sunny Side Country Club help keep track of golfer scores, and print those results onto the screen. Your program should do the following:
Have the program prompt the users for a name, then prompt again for that users golf score.
Ensure (validate) that the text entered for the users name is string, and scores entered are int.
Have the program write both the users name and golf score into a document called golfscores.txt.
Ask the user if there are golfers to add with a 'yes' or 'y', and if so, have it repeat the first two steps, until the user responds with a 'no' or 'n'.
After an 'no' or 'n' is entered, have the program print our all of the golfers names and scores onto the screen."""

username = input("What is your name?")


greeting = 'Hello ' + username + ' Welcome to Sunny Side Country Club.  This program will keep track of your golf scores so you can focus on the game!'
print(greeting)

def  main():
	another = 'y' 
	
	#open file to write

	golffile = open('golfscores.txt' , 'w')

	#write records to the file
	while another == 'y' or another == 'Y' or another == 'yes' or another == 'Yes':
		#get the data
		print('Enter the following data for golfer: ') 

		flag = 0
		while flag == 0:
		
			name = input("Golfer name: ")
			

			ascii_name = ord(name[0])

			if (ascii_name >= 65 and ascii_name <= 90) or (ascii_name >= 97 and ascii_name <=122):
				flag = 1
			else:
				print ('Names cannot start with a number or special character. Names must start with a letter. ')
		
		flag = 0
		while flag == 0:
			try:
				hole = int(input("Hole number: "))
			except ValueError:
				print('Please enter a whole number')
			else:
				flag = 1

		flag = 0
		while flag == 0:
			try:
				myScore = int(input("Golf score: "))
			except ValueError:
				print('Please enter a whole number')
			else:
				flag = 1



		#write the data to the file

		golffile.write(name + '\n')
		golffile.write(str(hole) + '\n')
		golffile.write(str(myScore) + '\n')

		#Determine if user wants to add another entry

		print('Do you want add anymore players and scores?')
		
		another = input('Type y or yes to add more.  To quit type n or no ')
		while(another != 'y' and another != 'yes' and another != 'n' and another != 'no'):
			print('Incorrect input.  Please type y or yes to add more.  To quit type n or no ')
			another = input('Type y or yes to add more.  To quit type n or no ')

		
 
	golffile.close()
	print()
	print('Golf scores added to golfscores.txt')
	print()



#this program displays the data

def display():
		#open the golfscores.txt file
		golffile = open('golfscores.txt' , 'r')

		#read the first record description field

		name = golffile.readline()

		#read the file
		while name != '':

			#read the hole field

			hole = golffile.readline()
			#read the score field
			myScore = golffile.readline()

			#strip the \n 

			name = name.rstrip('\n')
			hole = hole.rstrip('\n')
			myScore = myScore.rstrip('\n')

			#display the record
			print('Golfer name: ' , name)
			print('Hole: ' , hole)
			print('Golf score: ' , myScore)

			#read the next description

			name = golffile.readline() 

		#close the file

		golffile.close()



main()
display()


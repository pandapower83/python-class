"""precipitationprogramv6.py This program tracks precipitation for users around the world.
made by Rachel Winchel CIS 121 Spring 2018. 
Have the program prompt the user for the amount of precipitation, using the name of the month, starting with January.
Then use a list or tuple to store the names of the month.
Have the program validate that the data is int, then store the precipitation data given into a list.
Once all twelve months data have been collected, have the program display the following (Using Labels Please):
Total amount of rainfall. 
Month with most Rainfall
Month with the least rainfall
Average rainfall for all months
Have these numbers and labels written to a document labels rainFall.txt
Ask the user if they have another year of data to add, and if 'yes' or 'y', then have the program execute again.
If the response is 'no' or 'n', then have the program print onto the screen all the data stored in the document rainFall.txt"""

#global definitions
#Create a list to store the name of the months
month_Names = ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' ,'October' , 'November', 'December']
#Create a variable to hold an index
index = 0

another = 'y'

#global variables mostRainfallMonth and leastRainfallMonth need the name of a month from the month_Names list.
totalYearRainfall = 0
mostRainfallMonth = ''
leastRainfallMonth = ''
averageYearRainfall = 0
#create a list to hold the rain data for each month
monthlyRainfall = [0] * len(month_Names)

#precipitationfunction
def precipitation():
	index = 0
	
	# Get the rainfall amount for each month
	
	for index in range(len(month_Names)):
		flag = 0
		while flag == 0:
			try:
				#months[index] = int(input('Enter the amount of rainfall in ' + month_Names[index] + ': '))
				monthlyRainfall[index] = int(input('Enter the amount of rainfall in ' + month_Names[index] + ': '))
				#index += 1
			except ValueError:
				print('Please enter a whole number')
			else:
				flag = 1

def CalcRainfallTotal():
	global totalYearRainfall
	global	monthlyRainfall
	#calculate the total of the list elements in monthlyRainfall list
	for value in monthlyRainfall:
		totalYearRainfall += value

	#display the total of the list elements
	print('The total inches of rainfall for the year is: ', totalYearRainfall)

def CalcAverageRainfall():
	global totalYearRainfall
	global monthlyRainfall
	global month_Names
	global averageYearRainfall
	
	#calculate the average of the elements
	averageYearRainfall = totalYearRainfall / len(monthlyRainfall)

	#display the total of the list of elements
	print('The average rainfall for the year is ' , averageYearRainfall)

def CalcMaxRainfall():
	global mostRainfallMonth
	global monthlyRainfall
	global month_Names

	maxRainfall = -1
	maxRainfallPos = -1

	for i in range(len(month_Names)):
		if monthlyRainfall[i] > maxRainfall:
			maxRainfall = monthlyRainfall[i]
			maxRainfallPos = i

	mostRainfallMonth = month_Names[maxRainfallPos]
	print('The month with the most rainfall is ' , mostRainfallMonth)

def CalcMinRainfall():
	global leastRainfallMonth
	global monthlyRainfall
	global month_Names

	minRainfall = -1
	minRainfallPos = -1

	for i in range(len(monthlyRainfall)):
		if monthlyRainfall[i] < minRainfall or minRainfallPos == -1:
			minRainfall = monthlyRainfall[i]
			minRainfallPos = i

	leastRainfallMonth = month_Names[minRainfallPos]
	print('The month with the least rainfall is ' , leastRainfallMonth)


def clearData():
	global totalYearRainfall
	global averageYearRainfall

	totalYearRainfall = 0
	averageYearRainfall = 0



def writeFile():
	global totalYearRainfall
	global monthlyRainfall
	global month_Names
	global averageYearRainfall
	global mostRainfallMonth
	global leastRainfallMonth

	weatherDataFile = open('rainFall.txt' , 'w')

	
	#weatherDataFile.write(str(monthlyRainfall) + '\n')
	for i in range (len(month_Names)):
		weatherDataFile.write(month_Names[i] + " rainfall total is:  " + str(monthlyRainfall[i]) + '\n')
	weatherDataFile.write("The total amount of rainfall for the year is: " + str(totalYearRainfall) + '\n')
	weatherDataFile.write("The average amount of rainfall for the year is: " + str(averageYearRainfall) + '\n')
	weatherDataFile.write("The month with the most rainfall is: " + mostRainfallMonth + '\n')
	weatherDataFile.write("The month with the least rainfall is: " + leastRainfallMonth + '\n')

	weatherDataFile.close()
	print()
	print('Precipitation data added to rainFall.txt')
	print()



def main():
	global another
	while True:
		if another == 'y' or another == 'Y' or another == 'yes' or another == 'Yes':

			clearData()
			precipitation()
			CalcRainfallTotal()
			CalcAverageRainfall()
			CalcMinRainfall()
			CalcMaxRainfall()
			writeFile()

			print('Do you want add another year of precipitation data?')
			another = input('Type y or yes to add more.  To quit type n or no ')
			print()

		elif another != 'y' and another != 'yes' and another != 'n' and another != 'no':
			print('Incorrect input.  Please type y or yes to add more.  To quit type n or no ')
			another = input('Type y or yes to add more.  To quit type n or no ')
		elif another == 'n' or another == 'no':
			break
			

def display():

	print('The following data is from rainFall.txt')
	weatherDataFile = open('rainFall.txt' , 'r')

	#read the first record description field

	for line in weatherDataFile:
		print (line.rstrip('\n'))

	weatherDataFile.close()
		
main()
display()

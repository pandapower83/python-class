"""phone pad assignment final.py
In this assignment, you are going to make a phone number converter. Whenever you see a number like 888-BUY-GAME, you'll be able to convert it to the actual number 888-289-4263. Have your program complete the following.

Have the user enter the number with the format xxx-xxx-xxxx, like the example 888-BUY-GAME.
Have the program convert the string to lower case. (This will make life easy)
Have the program 'decide' if the string element is an alphabetic character, and if so, convert it to a number. 
Hint: Create two lists that store your lower case letters, and your numeric keypad numbers.
Hint: Remember, each number on the keypad has several letter values.
Have the program print on the screen, in one line, the phone number, following this example 123-345-5678."""

#get the phone number here
myChar = input("Enter a phone number in the format xxx-xxx-xxxx, like the example 888-BUY-GAME. \n")

#make the letters lowercase
myChar = myChar.lower()


#creating 2 lists to store my letters and my numbers
# Added " " for number 1, because it does not have any char assigned to it, but we
# want to keep lists the same length.
letterList = [" ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz", " "]     											
numberList = ["1", "2","3","4","5","6","7","8","9", "0"]
myNumberPos = ''

#for the letter in the range of the length of the phone number that was inputted
for j in range(len(myChar)):
#if the character is actually a-z and not something random or a number
  if ord(myChar[j]) >= 97 and ord(myChar[j]) <= 122:
    #for the letter in the range of the length of my letters list
    for index in range(len(letterList)):

    # Get letterList element and search myChar using find function and save it in pos. We are finding the letter j that was given in the input
    # and looking for it in the letter list and storing that position in pos

    
      pos = letterList[index].find(myChar[j])
      #if the position does not equal -1 meaning that the letter was found. the three element positions are 0, 1, 2 so -1 means it isn't in there.
      if pos != -1:
        myNumberPos += numberList[index]
        break
  #if it is a number like 888 or 800 or whatever then it automatically stores and saves that
  else:
     myNumberPos += myChar[j]
    

print(myNumberPos)


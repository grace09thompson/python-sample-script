# Name: Grace Thompson
#
# This program creates 3 files in the same directory as the script. Each file
# contains 10 random characters from the lowercase alphabet with no spaces in between.
# The program will print out the contents of the three files to the screen, and then
# print out two random integers between 1 - 42, inclusive, and the product of the
# two numbers.

import random
import string

# Function returns a string of 10 random characters from the lowercase alphabet
def getRandomString():
	randStr = ""
	
	for n in range(10):
		#generate random lowercase character
		lchar = random.choice(string.ascii_lowercase)
		randStr = randStr + lchar
	return randStr


# Main function definition
def main():
	# generate random seed so sequence is not generated again in future execution
	random.seed()

	print('\nWelcome to a simple Python program!\n')
	print('This program creates three files and writes to each')
	print('a string of 10 randomly generated lowercase characters.')
	print('The program also randomly generates two numbers between 1 and 42 ')
	print('and displays their sum.\n')

	#get randomly generated string of lowercase characters
	string1 = getRandomString()
	#open a file and write string to file, ending in newline character
	outputFile = open('FILE1.txt', 'w')
	outputFile.write(string1 + '\n')
	#close file
	outputFile.close()

	print(string1 + '\n')
	
	#get second string
	string2 = getRandomString()
	#open a file and write string to file
	outputFile = open('FILE2.txt', 'w')
	outputFile.write(string2 + '\n')
	outputFile.close()

	print(string2 + '\n')
	
	# do the same for the third string
	string3 = getRandomString()
	outputFile = open('FILE3.txt', 'w')
	outputFile.write(string3 + '\n')
	outputFile.close()

	print(string3 + '\n') 
	
	# generate two random integers between 1 and 42 inclusive
	num1 = random.randint(1, 42)
	print(num1)

	num2 = random.randint(1, 42)
	print(num2)

	intSum = num1 + num2
	print('sum: ' + str(intSum) + '\n')

# Call the main function
main()

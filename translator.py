"""
Al Bhed Translator
Author: Rob Merrill / legolicious / Learn.Build.Deploy / slash / /
Version: 1.0

Bidirectional English/Al Bhed command-line translator.
"""

################################ DICTIONARIES #################################

# Stores each language's alphabet as a string
english = 'abcdefghijklmnopqrstuvwxyz'
alBhed = 'ypltavkrezgmshubxncdijfqow'

# zip() essentially takes each letter from an alphabet and pairs it with the 
# letter in the matching position from the other alphabet. We're placing those pairs into 
# a dictionary and storing them in these variables 

englishToAlBhed = dict(zip(english, alBhed))
alBhedToEnglish = dict(zip(alBhed, english))

################################## FUNCTIONS ##################################

def translate(text, dictionary):
	"""Translate input text to selected language"""
	
	# Stores the result of a translation
	result = ""

	# Loops through input text one character at a time
	for characters in text:
		# .lower() converts character to lowercase to match dictionary keys
		# .get() looks for character in selected dictionary
		# characters is a fallback value for characters not in the dictionary
		#  (spaces, numbers, punctuation marks, etc.)
		character = dictionary.get(characters.lower(), characters)
		
		# Checks if original character is uppercase, applies to translated
		#  character
		if characters.isupper():
			character = character.upper()

		# Adds the translated character to the result string
		result += character 

	# Sends completed translation to where it was called
	return result

def main():
	"""
	This function allows the user to select languages and input text to
	translate.
	"""
	while True:

		# User selects language
		language = input("Language to translate to (English/Al Bhed): ").lower()
		
		# Selects language based on user input
		if language == 'english':
			dictionary = alBhedToEnglish
		elif language == 'al bhed':
			dictionary = englishToAlBhed
		else:
			# Error handling for invalid input.
			print("ERROR: Invalid selection. Please choose English or Al Bhed.\n")
			continue

		while True:
			# User inputs text to translate...
			text = input('Enter text to translate: ')

			# Passes user input to translate function and prints it to console
			print(f'Translation: {translate(text, dictionary)}\n')
			
			# Presents user with three choices
			choice = ''
			while choice not in ('1', '2', '3'):
				choice = input('1. Continue translating\n2. Change language\n3. Quit\n\nSelection: ')
				print()
			
			if choice == '1':
				# Lets user continue translating to currently selected language
				continue
			elif choice == '2':
				# Brings user back to language selection loop
				break
			elif choice == '3':
				# Exits the program
				return

main()

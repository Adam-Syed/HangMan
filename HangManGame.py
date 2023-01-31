import random
import string
from HangManGraphics import HANGMANPICS

"""
Hangman!
1) Start off with all of the letters and 8 lives
2) You are shown _ for each of the letters you have to guess
3) If you guess correctly the _ changes to that letter
4) If you guess incorectly the _ stays the same and you lose a life
5) Keep guessing until you have no lives left

"""
alphabet = dict.fromkeys(string.ascii_uppercase, False) # Dictionary to state whether a value has been guessed before or not. False = not guessed.

def GenerateWord() -> str:
	# This function will go through the Word Corpus and randomly select a single word -> RANDOM
	file = open("WordsCorpus", "r")
	words = file.readlines()
	file.close()
	FinalWord = random.choice(words).strip().upper()
	return str(FinalWord)

def ConvertUnderscore(Word: str, CorrectLetters: list):
	# This function will take a word and check it against the list of all the correctly guessed letters. It will print the answer as _'s but will leave the correct letters.
	ConvertedList = []
	for char in Word:
		if char in CorrectLetters:
			ConvertedList.append(char)
		else:
			ConvertedList.append("_")
	return " ".join(ConvertedList)

def GuessCheck(Word, Guess):
	# This function will check whether their guess is correct.
	Guess = str(Guess)
	alphabet[Guess] = True # First change guessed letter status to True so that we will know in the future they have already guessed this letter.

	if Guess in Word:
		return True
	else:
		return False

def decor(func):
	# This function will decorate the game function with "=" to format it and make it look nicer.
	def wrap():
		print("\n=====================================================================================================")
		func()
		print("\n==========================================================================================")
	return wrap

@decor
def Game(): 
	# This is the function in which the user will play the game.
	print(f"\nWelcome to Hangman! Try and guess the word by entering letters but be careful; you only have 8 lives!")
	
	while True:
		Lives = 8
		PicsCounter = 0
		CorrectLetters = []
		Answer = GenerateWord()
		UnderScoredAnswer = ConvertUnderscore(Answer, CorrectLetters)

		print(UnderScoredAnswer)

		while Lives > 0:
			RemainingLetters = [i for i, char in alphabet.items() if char == False]
			print("\nRemaining Letters:", "  ".join(RemainingLetters))
			print("\nLives: ", Lives)
			print(HANGMANPICS[PicsCounter])


			try:
				if set(Answer) == set(CorrectLetters):
					print(f"\nYou have correctly guessed the word! {Answer}")
					file = open("Congrats", "r")
					print(file.read())
					file.close()
					break

				else:

					Guess = input("\nPlease Choose a Letter: ").upper()

					if alphabet[Guess] == True:
						print("\n\n\nYou have already guessed this letter!")
						continue
					elif GuessCheck(Answer, Guess) == True:
						print(f"\n\n\nThe letter {Guess} is in the Word!")
						CorrectLetters.append(Guess)
						print(ConvertUnderscore(Answer, CorrectLetters))
					else:
						print(f"\n\n\nThe letter {Guess} is NOT in the Word!")
						Lives -= 1
						PicsCounter += 1
						print(ConvertUnderscore(Answer, CorrectLetters))
					
			except KeyError:
					print("\nPlease make sure you have chosen a Letter from the English Alphabet")
			except ValueError:
				print("\nPlease make sure you have chosen only 1 Letter")
			except TypeError:
				print("\nPlease make sure you have chosen a Letter from the English Alphabet")

			if Lives == 0:
				print(f"\nYou were unable to guess the correct word :( The word was: {Answer}")
				print("\n")
				file = open("Unlucky", "r")
				print(file.read())
				file.close()

		PlayAgain = input("\n\nWould you like to play again? (y/n)  ")

		if PlayAgain == "y":
			print("\n\n")
			continue
		else:
			break

Game()
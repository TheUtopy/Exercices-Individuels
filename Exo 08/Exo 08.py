# Mastermind
import random

colors = ["yellow", "red", "black", "blue", "green", "orange", "purple", "white"]


def make_combination(number_of_player=1):
	"""
	Initialize the combination to guess
	:param number_of_player:
	:return: A list of 4 strings containing the combination to guess
	"""
	combination = []
	if number_of_player == 1:
		for i in range(4):
			combination.append(random.choice(colors))
	return combination


def ask_a_color():
	"""
	Ask player for a color and check is the color is valid or not and ask again while it's not a valid one
	:return: A string containing a color
	"""
	color = input()
	while not check_guessed_color(color):
		color = input(f"The color you choose is not valid. Choose between those colors : {colors}\n")
	return color


def check_guessed_color(color):
	"""
	:param color:
	:return: True if the color guessed by the player is valid. Else return False
	"""
	if color in colors:
		return True
	else:
		return False


def try_to_guess():
	"""
	Ask for a combination of four colours to the player.
	:return: Combination of 4 colors in a list of strings
	"""
	print(f"Try to guess the combination.\nThe possible colors are {colors}")
	print("What's the first color ?")
	color1 = ask_a_color()
	print("What's the second color ?")
	color2 = ask_a_color()
	print("What's the third color ?")
	color3 = ask_a_color()
	print("What's the last color ?")
	color4 = ask_a_color()
	combination = [color1, color2, color3, color4]
	print(f"Your combination is : {combination}")
	return combination


def is_guess_right(combination_to_guess, guessed_combination):
	"""
	Check if the combination guessed by the player have its colours in the right position, the right colour but misplaced or if the colour isn't used in the combination to guess.
	:param combination_to_guess:
	:param guessed_combination:
	:return: Nothing (the purpose is to print something)
	"""
	missed = 0
	misplaced = 0
	right_position = 0
	for i in range(4):
		if guessed_combination[i] in combination_to_guess:
			if guessed_combination[i] == combination_to_guess[i]:
				right_position += 1
			else:
				misplaced += 1
		else:
			missed += 1

	print(f"You have {right_position} correctly placed, {misplaced} misplaced and {missed} missed.")


def game():
	combination_to_guess = make_combination()
	number_of_guessing = 3
	guessed_combination = try_to_guess()
	number_of_guessing -= 1
	while guessed_combination != combination_to_guess and number_of_guessing != 0:
		is_guess_right(combination_to_guess, guessed_combination)
		print(f"You have {number_of_guessing} guess remaining.")
		guessed_combination = try_to_guess()
		number_of_guessing -= 1
	if guessed_combination == combination_to_guess:
		print('Yay ! You won !')
	elif number_of_guessing == 0:
		print("You lost ! You're so bad at this game !")
		print(f"The correct combination was : {combination_to_guess}")


game()

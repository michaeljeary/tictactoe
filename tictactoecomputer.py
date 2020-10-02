from random import randint
# Global Variables

# empty game board
board = ["-", "-", "-",
		 "-", "-", "-", 
		 "-", "-", "-"]

# If the game is still going, run loop. Only flase when game over.
game_still_going = True

# Who won? or tie?
winner = None

# Who's turn is it?
user_player = "X"
computer_player = "O"

def play_game():
	# Display the initial board before starting
	display_board()

	# Make a loop over and over until game is over
	while game_still_going:
		# Handle a turn
		handle_turn(user_player)
		# Check if game is over
		check_game_over()
		# Handle a computer turn
		handle_computer_turn(computer_player)
		# If game is not over, flip to other player
		flip_player()

	
	if winner == "X":
		print("Congratulations, you won!")
	elif winner == "O":
		print("Bummer, the computer beat you.")
	elif winner != "X" or "O":
		print("Boring. A tie.")	

# define our board
def display_board():
	print("\n")
	print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
	print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
	print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
	print("\n")

# Add random player goes first	

# Handle each turn
def handle_turn(player):

	print(player + "'s turn.")
	# get the position that the player wantst to use
	position = input("Choose a postion from 1-9: ")

	# while running not valid. Make sure in range. Change to board position. Check if position is available.
	# if it is, place it. If it isn't reloop.
	valid = False
	while not valid:

		# if will only ask once. While will continuouslly until the right input is put.
		while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			position = input("Invalid choice. Choose a postion from 1-9: ")

		# postion will be an integer so make it so. Subtract 1 to account for 0-8 on our board
		position = int(position) - 1

		# Making it so you cant overwrite a spot already taken.
		if board[position] == "-":
			valid = True
		else:	
			print("Position already taken. Try again.")

	# Once we get position, put it in
	board[position] = user_player
	# Then display the choice
	display_board()

def handle_computer_turn(computer):

	print(computer + "'s turn.")
	input("Press any key to allow the computer to go.")

	valid = False
	while not valid:
		computer_position = int(f"{randint(0,8)}")
		
		if board[computer_position] == "-":
			valid = True
		elif board[computer_position] == "X":
			valid = False
		elif board[computer_position] == "O":
			valid = False		
		else:
			return None
	
	# Once we get position, put it in
	board[computer_position] = computer
	# Then display the choice
	display_board()	

def check_game_over():
	# Call two more functions: win or tie. Two criteria for game ending
	check_for_winner()
	check_if_tie()

def check_for_winner():
	# Set up global variable
	global winner
	# Check rows
	row_winner = check_rows()
	# Check columns
	column_winner = check_columns()
	# Check diagonal
	diagonal_winner = check_diagonals()
	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None
	
# Check each for 3 in a row, then return X or O, then quit the game.
def check_rows():
		# Set up global variables
	global game_still_going
	# pick out each element. If they're all equal, return winner.
	# But cannot be equal to a -
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"

	# if any row is a winner, stop the game
	if row_1 or row_2 or row_3:
		game_still_going = False

	# tells us if winner is X or O	
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]
	else:
		return None

def check_columns():

	global game_still_going

	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"

	if column_1 or column_2 or column_3:
		game_still_going = False

	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]
	else:
		return None			

def check_diagonals():

	global game_still_going

	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[6] == board[4] == board[2] != "-"

	if diagonal_1 or diagonal_2:
		game_still_going = False

	if diagonal_1:
		return board[0]
	elif diagonal_2:
		return board[6]
	else:
		return None

def check_if_tie():
	# declare global
	global game_still_going
	
	if "-" not in board:
		game_still_going = False
		return True
	else:
		return False		

def flip_player():
	# Global we need
	global user_player
	global computer_player

	# if current player was X, change to O
	if user_player == "X":
		computer_player = "O"
	else:
		user_player = "O"
		
play_game()	

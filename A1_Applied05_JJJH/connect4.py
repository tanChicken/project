"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
"""
import random
import os

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")


def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
	# Implement your solution below

	# Assigns loop variable
	i = 0

	# Loops until a valid input is entered
	while i == 0:
		# Stores the user input
		user_input = input(prompt)
		# Checks if the input is valid
		if user_input in valid_inputs:
			# If it is valid, returns the input and terminates the loop by updating loop variable
			return user_input
			i = 1		
		else:
			# If input is invalid, prints message and repeats the loop
			print("Invalid input, please try again.")


def create_board():
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	# Implement your solution below
	# raise NotImplementedError

	# Creates a 2D list of 0s with 6 rows and 7 columns
	board = [[0 for i in range(7)] for j in range(6)]
	return board


def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	# Player symbols to be used in the board in array for ease of changing and scaling
	player_symbols = ["X", "O"]

	# Prints the board header consisting the game name and player symbol
	print("=" + " Connect4 ".center(len(board[0]) * 4, "="))
	print("{:<{width_1}}{:>{width_2}}\n".format(
		"Player 1: {}".format(player_symbols[0]), 
		"Player 2: {}".format(player_symbols[1]), 
		width_1 = len(board[0]) * 2 + 1, 
		width_2 = len(board[0]) * 2
	))

	# Prints the play area of the board and its contents
	for i in range(len(board[0])):
		print("  {}".format(i + 1), end = "")
		if (i + 1) < len(board[0]): print(" ", end = "")
	print()

	for i in range(len(board[0])):
		print(" ---", end = "")
	print()

	for i in range(len(board)):
		print("|", end = "")
		for j in range(len(board[i])):
			print(" {} ".format(" " if board[i][j] == 0 else player_symbols[board[i][j] - 1]), end = "|")
		print()
		for i in range(len(board[0])):
			print(" ---", end = "")
		print()

	# Prints the bottom row of the board
	for i in range(len(board[0]) * 4 + 1):
		print("=", end = "")
	print()


def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player who is dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	# Implement your solution below

	# Enforces that the Player's number must only be 1 or 2
	if player not in [1, 2]:
		raise ValueError("Player's piece must be either 1 or 2.")
		
	# Adjusts the column index to start from zero
	column = column - 1

	# Iterates through the rows from the bottom to the top
	for row in reversed(range(len(board))):
		# If the current cell is empty, drops the Player's piece
		if board[row][column] == 0:
			board[row][column] = player
			return True
			
	# Piece cannot be dropped because the column is full
	return False


def execute_player_turn(player, board):
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below

	# Enforces that the Player's number must only be 1 or 2
	if player not in [1, 2]:
		raise ValueError("Player's token must be either 1 or 2.")

	# Assigns loop variable
	i = 0

	# Loops until a valid input is entered
	while i == 0:

		# Prompts Player to enter a valid column number
		column = int(validate_input("Player " + str(player) +", please enter the column you would like to drop your piece into: ", ["1", "2", "3", "4", "5", "6", "7"]))
		# Checks if the drop is successful
		if drop_piece(board, player, column) == True:
			# If it is, returns the chosen column number, updates loop variable and terminates the loop
			i = 1
			return column
		else:
			# If the chosen column is full, prints message and continues the loop
			print("That column is full, please try again.")


def end_of_game(board):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    rows = len(board)
    columns = len(board[0])

    connected = 0

    # Starts the board check from the bottom row up
    for i in range(rows - 1, -1, -1):
        # Alternates checking between Player 1 and Player 2 
        for j in range(1, 3):
            # Iterates through each column for each row
            for k in range(columns):
                # Checks for horizontal win
                if k <= 3:
                    if(board[i][k] == j and board[i][k + 1] == j and board[i][k + 2] == j and board[i][k + 3] == j):
                        connected = 1
                        return j
                # Ensures that the rows iterated are the bottom 3 rows since the checking method is
                # to check 4 consecutive cells at once
                if i >= 3:
                    # Checks for vertical win
                    if(board[i][k] == j and board[i - 1][k] == j and board[i - 2][k] == j and board[i - 3][k] == j):
                        connected = 1
                        return j
                    # Checks for bottom left to top right diagonal win
                    if k <= 3 and board[i][k] == j and board[i - 1][k + 1] == j and board[i - 2][k + 2] == j and board[i - 3][k + 3] == j:
                        connected = 1
                        return j
                    # Checks for top left to bottom right diagonal win
                    if k >= 3 and board[i][k] == j and board[i - 1][k - 1] == j and board[i - 2][k - 2] == j and board[i - 3][k - 3] == j:
                        connected = 1
                        return j

	# Checks the state of the game if there are no wins
    if not connected:
        for row in range(len(board)):
            row = board[row]
            if 0 in row:    # If there are still empty cells, game is still ongoing
                return 0
            else:
                return 3    # No more empty cells, the game is a draw


def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# Implement your solution below
	
	# To create a new game board
	board = create_board()

	# Assigns the first turn to Player 1
	player = 1

	# Sets the winner 0 (game not over)
	winner = 0

	# Creates an empty list to store the moves played
	moves_list = []


	# Game loop that continues until there is a winner or a draw
	while winner == 0:

		# Clears the console
		clear_screen()

		# Prints the current state of the board
		print_board(board)

		# Checks if any moves has been played
		if len(moves_list) > 0:
			
			# Retrieves the most recent move from moves_list
			previous_drop = moves_list[-1]
			# If a successful drop was made, prints a message that displays the Player and the column that the piece was dropped into
			print("Player", previous_drop["player"], "dropped a piece into column", previous_drop["column"])

		# Stores column number returned by execute_player_turn
		chosen_column = execute_player_turn(player, board)
		# Stores the previous Player's move in dictionary format and appends it to moves_list
		moves_list.append({"player": player, "column": chosen_column})

		# Checks if the game has ended based on the functions in end_of_game
		winner = end_of_game(board)
		
		# Game not over
		if winner == 0:
			# Players switch turns
			player = 1 if player == 2 else 2
		# Sets the winner to 3 to represent a draw
		elif winner == 3:
			winner = 3
        
	# Prints the final state of the board
	print_board(board)

	if winner == 3:
		# If the game is a draw, prints the following message
		print("Draw!")
	else:
		# If there is a winner, prints random winning statements
		winner_statements = [
			"Player " + str(winner) + " wins!",
			"Player " + str(winner) + " is the winner!",
			"Congratulations! Player " + str(winner) + " beats Player " + str(3 - winner) + ".",
			"Player " + str(winner) + " outsmarted Player " + str(3 - winner) + "!",
			"Player " + str(winner) + " emerges victorious!"
    	]
		print(random.choice(winner_statements))


def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	# Assigns loop variable to "0"
	user_select = "0"

    # Loops until user selects to exit
	while user_select != "4":
		
        # Clears the console
		clear_screen()
		
        # Prints the Main Menu
		print("=============== Main Menu ===============")
		print("Welcome to Connect 4!")
		print("1. View Rules")
		print("2. Play a local 2 player game")
		print("3. Play a game against the computer")
		print("4. Exit")
		print("=========================================")
		
        # Prompts user for a valid Main Menu input
		user_select = validate_input("Please enter your choice: ", ["1", "2", "3", "4"])

		# Processes user input
		if user_select == "1": # Views rules
			clear_screen()
			print_rules()
			input("Click Enter to return to the Main Menu. ")
			
		elif user_select == "2": # Plays a local 2 player game
			clear_screen()
			local_2_player_game()
			input("Click Enter to return to the Main Menu. ")
			
		elif user_select == "3": # Plays a game against the computer
			clear_screen()
			cpu_player_choice = int(validate_input(
					"Please select a difficulty level (1 => Easy, 2 => Medium, 3 => Hard): ", 
					["1", "2", "3"]))
			
			game_against_cpu(cpu_player_choice)
			input("Click Enter to return to the Main Menu. ")
			
		elif user_select == "4": # Exits the game
			clear_screen()
			print("Thank you for playing Connect 4. Until next time!")
			


def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	
	# Assigns loop variable 'successful_drop' to False
	successful_drop = False

    # Loops until there is a successful drop
	while successful_drop != True:
		# Attempts to drop a piece into a random column
		random_column = random.randint(1, 7)
                
		# If successful, updates successful_drop to True
        # Terminates loop and returns the random column
		successful_drop = drop_piece(board, player, random_column)
	return random_column
	

def horizontal_win(board):

    # Iterates through each row on the board until the last row
    for row in range(0, len(board)):
        
        # Iterates from the 1st to the 4th column
        for column in range(0, 4):
            player = board[row][column]

            # Checks that the current cell is not empty
            if player != 0:
                # If next three cells in the row have the same value as the current cell, return the Winner's number
                if player == board[row][column + 1] == board[row][column + 2] == board[row][column + 3]:
                    return player

    return 0    # No horizontal win detected
        

def vertical_win(board):

    # Iterates from the 1st to 3rd row
    for row in range (0, 3):

        # Iterates through each column until the last column
        for column in range(0, 7):
            player = board[row][column]

            # Checks that the current cell is not empty
            if player != 0:
                # If next three cells in the column have the same value as the current cell, return the Winner's number
                if player == board[row + 1][column] == board[row + 2][column] == board[row + 3][column]:
                    return player

    return 0 # No vertical win detected
    

def diagonal_win(board):

    # Iterates from the 4th row to the last row
    for row in range(3, len(board)):

        # Iterates from the 1st to the 3rd column
        for column in range(0, 4):
            player = board[row][column]

            # Checks that the current cell is not empty
            if player != 0:
                # Checks for a bottom-left to top-right connection
                if player == board[row-1][column+1] == board[row-2][column+2] == board[row-3][column+3]:
                    return player

    # Iterates from the 1st to 3rd row
    for row in range(0, 3):

        # Iterates from the 1st column to the 4th column
        for column in range(0, 4):
            player = board[row][column]

            # Checks that the current cell is not empty
            if player != 0:
                # Checks for a top-left to bottom-right connection
                if player == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3]:
                    return player

    return 0    # No diagonal win detected


def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty. 
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""

	# Determines Player number
	opponent = 1 if player == 2 else 2

    # Checks for immediate win
	for column in range(7):
		for row in reversed(range(len(board))):
			if board[row][column] == 0:
                # Tries dropping the player's piece to see if it results to a win
				board[row][column] = player
				if horizontal_win(board) == player: 
					return column + 1
				elif vertical_win(board) == player:
					return column + 1
				elif diagonal_win(board) == player:
					return column + 1
				else:
                    # Undos the drop if it doesn't result to an immediate win
					board[row][column] = 0
				break	# Breaks out of the inner loop to move to the next column


    # Checks for opponent's potential immediate win and blocks it
	for column in range(7):
		for row in reversed(range(len(board))):
			if board[row][column] == 0:
                # Tries dropping the opponent's piece to see if it results to a win
				board[row][column] = opponent
				if horizontal_win(board) == opponent:
					# Blocks the win
					board[row][column] = player
					return column + 1
				elif vertical_win(board) == opponent:
					# Blocks the win
					board[row][column] = player
					return column + 1
				elif diagonal_win(board) == opponent:
					# Blocks the win
					board[row][column] = player
					return column + 1
				else:
                    # Undos the drop if there is no potential immediate win for the opponent
					board[row][column] = 0
				break	# Breaks out of the inner loop to move to the next column


    # Random drop if no immediate win or block
	successful_drop = False
	
	while successful_drop != True:
		random_column = random.randint(1, 7)
		successful_drop = drop_piece(board, player, random_column)
		
	return random_column


def cpu_player_hard(board, player):
    """
    Executes a move for the CPU on hard difficulty.
	This function creates a copy of the board to simulate moves.

    It first checks for an immediate win and plays that move if possible. 
    If no immediate win is possible, it checks for an immediate win 
    for the opponent and blocks that move. If neither of these are 
    possible, it plays in the center columns (4, 3 and 5) to get more
    winning combinations. If all the specified cells in the center columns  
    are occupied, it plays a random move.
    
    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """

    # Determines Player number
    opponent = 1 if player == 2 else 2

    # Checks for immediate win
    for column in range(7):
        for row in reversed(range(len(board))):
            if board[row][column] == 0:
                # Tries dropping the player's piece to see if it results to a win
                board[row][column] = player
                if horizontal_win(board) == player: 
                    return column + 1
                elif vertical_win(board) == player:
                    return column + 1
                elif diagonal_win(board) == player:
                    return column + 1
                else:
                    # Undos the drop if it doesn't result to an immediate win
                    board[row][column] = 0
                break # Breaks out of the inner loop to move to the next column

    # Checks for opponent's potential immediate win and blocks it
    for column in range(7):
        for row in reversed(range(len(board))):
            if board[row][column] == 0:
                # Tries dropping the opponent's piece to see if it results to a win
                board[row][column] = opponent
                if horizontal_win(board) == opponent:
                    # Blocks the win
                    board[row][column] = player
                    return column + 1
                elif vertical_win(board) == opponent:
                    # Blocks the win
                    board[row][column] = player
                    return column + 1
                elif diagonal_win(board) == opponent:
                    # Blocks the win
                    board[row][column] = player
                    return column + 1
                else:
                    # Undos the drop if there is no immediate win possible for the opponent
                    board[row][column] = 0
                break # Breaks out of the inner loop to move to the next column
                

    # Prioritizes center columns
    if board[5][3] == 0:  
        drop_piece(board, player, 4)
        return 4
    elif board[4][3] == 0:  
        drop_piece(board, player, 4)
        return 4
    elif board[5][4] == 0: 
        drop_piece(board, player, 5)
        return 5
    elif board[4][4] == 0:  
        drop_piece(board, player, 5)
        return 5
    elif board[5][2] == 0: 
        drop_piece(board, player, 3)
        return 3
    elif board[4][2] == 0: 
        drop_piece(board, player, 3)
        return 3
    elif board[3][3] == 0:  
        drop_piece(board, player, 4)
        return 4
    elif board[3][2] == 0: 
        drop_piece(board, player, 3)
        return 3
    elif board[3][4] == 0: 
        drop_piece(board, player, 5)
        return 5
    elif board[2][3] == 0:  
        drop_piece(board, player, 4)
        return 4
    elif board[2][2] == 0: 
        drop_piece(board, player, 3)
        return 3
    elif board[2][4] == 0: 
        drop_piece(board, player, 5)
        return 5
    
    # Random drop if no strategic move is found
    successful_drop = False
    while successful_drop != True:
        random_column = random.randint(1, 7)
        successful_drop = drop_piece(board, player, random_column)
    return random_column

    
def cpu_player_selector(difficulty, board, player):
	"""
	Selects the CPU player function based on the difficulty level.

	:param difficulty: The difficulty level of the CPU player.
	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: The CPU player function.
	"""
	match difficulty:
		case 1:
			return cpu_player_easy(board, player)
		case 2:
			return cpu_player_medium(board, player)
		case 3:
			return cpu_player_hard(board, player)
		

def game_against_cpu(cpu_player: int):
    """
    Runs a game of Connect 4 against the computer.

    :param cpu_player: The difficulty level of the CPU player. 1 => Easy, 2 => Medium, 3 => Hard.
    :return: None
    """
	
    board = create_board()
    game_end = 0

    # Stores last played player and column [local_player, cpu_player]
    local_last_played = [0, 0]
    cpu_last_played = [0, 0]

    # Game loop that stops when the game has ended
    while game_end == 0:
        clear_screen()
        print_board(board)

        # Prints local last played piece and corresponding player
        if(local_last_played[1] != 0):
            print("Player {} dropped a piece into column {}".format(local_last_played[0], local_last_played[1]))

        # Prints CPU last played piece and corresponding player
        if(cpu_last_played[1] != 0):
            print("Player {} dropped a piece into column {}".format(cpu_last_played[0], cpu_last_played[1]))

        # Stores local last played piece and corresponding player and executes player turn
        local_last_played[0] = 1
        local_last_played[1] = execute_player_turn(1, board)

        # Stores CPU's last played piece and corresponding player and executes player turn
        cpu_last_played[0] = 2
        cpu_last_played[1] = cpu_player_selector(cpu_player, board, 2)

        # Checks if game has ended
        game_state = end_of_game(board)

        # If the game has ended, terminates loop and prints the final board
        if game_state:
            game_end = 1
            clear_screen()
            print_board(board)

            winner_statements = [
                "Player {} wins!".format(game_state),
                "Player {} is the winner!".format(game_state),
                "Player {} emerges victorious!".format(game_state)
            ]

            # Prints the result of the game
            print(random.choice(winner_statements) if game_state != 3 else "Draw!")
            break

if __name__ == "__main__":
	main()
        
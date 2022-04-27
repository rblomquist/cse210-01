# -----Ricky Blomquist Tic Tac Toe game

board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

player_one = "X"
player_two = "O"


def main():
    game_over = False
    
    print_board(board)
    
    while not game_over:

        # Player one takes turn and calls functions to check board
        choice_one = int(input("Player 1, select number 1 - 9: "))
        board_choice(board, choice_one, player_one)
        print_board(board)
        game_over = check_board(board)

        # If player 1 has won the game then the loop ends
        # If not, player 2 takes their turn and checks the board again
        if not game_over:
            choice_two = int(input("Player 2, select number 1 - 9: "))
            board_choice(board, choice_two, player_two)
            print_board(board)
            game_over = check_board(board)



def print_board(board):
    """ function that prints the game board"""

    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def board_choice(board, choice, player):
    """Function that places the X or O based on user inputted number."""

    valid = False
    while not valid:
        # if statement to see if number is between 1 and 9
        if choice >= 1 and choice <= 9:
                # checks to see if that number already has a piece on it
                if board[choice -1] == "X" or board[choice -1] == "O":
                    print()
                    print("Square already taken")
                    choice = int(input("Select a different number 1 - 9: "))                   
                # otherwise puts X or O based on who's turn it is
                else:
                    board[choice - 1] = player
                    valid = True                
        else:
            print()
            print("Invalid choice")
            choice = int(input("Select number 1 - 9: "))


def check_board(board):
    """function to check the board to see if someone has won"""
    
    # --------------check vertical X -------------------
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("Player 1 wins!")
        game_over = True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("Player 1 wins!")
        game_over = True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("Player 1 wins!")
        game_over = True
    # --------------check vertical O -------------------
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("Player 2 wins!")
        game_over = True
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("Player 2 wins!")
        game_over = True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("Player 2 wins!")
        game_over = True
    # --------------check horizontal X -------------------
    elif board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("Player 1 wins!")
        game_over = True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("Player 1 wins!")
        game_over = True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("Player 1 wins!")
        game_over = True
    # --------------check horizontal O -------------------
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("Player 2 wins!")
        game_over = True
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("Player 2 wins!")
        game_over = True
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("Player 2 wins!")
        game_over = True
    # --------------check diagonal X -------------------
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("Player 1 wins!")
        game_over = True
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("Player 1 wins!")
        game_over = True
    # --------------check diagonal O -------------------
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("Player 2 wins!")
        game_over = True
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("Player 2 wins!")
        game_over = True

    else:
        game_over = False

    # -------------Checks for tie----------------------------
    count = 0 
    for each in board:
        if each == "X" or each == "O":
            count += 1
    if count == 9:
        print("It's a tie!")
        game_over = True

    return game_over


if __name__ == "__main__":
    main()





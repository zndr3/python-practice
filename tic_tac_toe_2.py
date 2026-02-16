
from random import randrange


def display_board(board):
    print(board)
    
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    try:
        display_board(board)
        move = int(input("Enter your move: "))
        if move > 0 and move < 10:
            for row in range(3):
                for col in range(3):
                    if board[row][col] == move:
                        board[row][col] = "O"
                        # print(victory_for(board, "O"))
                        if victory_for(board, "O"): 
                            # print("Returned to main loop after victory")
                            return True
                        
                        # print("returned to the main loop only")
                        return
            else:
                print("Input already taken. Please choose another move.")
                return enter_move(board)
        else:
            print("Please enter a number between 1 and 9.")
            return enter_move(board)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        return enter_move(board)
         

#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != "X" and board[row][col] != "O":
                free_fields.append((row, col))
    return free_fields
 

#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):

    if (board[0][0] == board[0][1] == board[0][2] == sign or
        board[1][0] == board[1][1] == board[1][2] == sign or
        board[2][0] == board[2][1] == board[2][2] == sign or
        board[0][0] == board[1][0] == board[2][0] == sign or
        board[0][1] == board[1][1] == board[2][1] == sign or
        board[0][2] == board[1][2] == board[2][2] == sign or
        board[0][0] == board[1][1] == board[2][2] == sign or
        board[0][2] == board[1][1] == board[2][0] == sign):
        if sign == "X":
            display_board(board)
            print("Computer wins!")
            return True
        else:
            display_board(board)
            print("You win!")
            return True
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


def draw_move(board):
    r_move = randrange(1, 10)
    print("Random move:", r_move)

    for row in range(3):
        for col in range(3):
            if board[row][col] == r_move:
                board[row][col] = "X"
                # print("Returned to main loop")
                if victory_for(board, "X"):
                    return True
                return
    else:
        print("Input already taken. Please choose another move.")
        return draw_move(board)



    # The function draws the computer's move and updates the board.


board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
while True:

    
    break

    if enter_move(board):
        break

    elif draw_move(board):
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break




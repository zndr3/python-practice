# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

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

    display_board(board)
    
    # scans the list if user input is valid
    
    try:
        # if make_list_of_free_fields(board):
            move = int(input("Enter your move: "))
            if move > 0 and move < 10:
                for row in range(len(board)):
                    for col in range(len(board[row])):
                        if board[row][col] == move:
                            board[row][col] = "O"
                            return
                            # if victory_for(board, "O"):
                            #     print("its suppose to break here")
                            #     return False
                            # else:
                            #     draw_move(board)
                else:
                    print("Input already taken. Please choose another move.")
                    # enter_move(board)
            else:
                print("Please enter a number between 1 and 9.")
                # enter_move(board)
        # else:
        #     print("It's a tie!")
        #     return False
        
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        # enter_move(board)
        
        
            
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
#     free_fields = []
#     for row in range(len(board)):
#         for col in range(len(board[row])):
#             if board[row][col] != "X" and board[row][col] != "O":
#                 free_fields.append((row, col))
#     return free_fields

    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):

#     if (board[0][0] == board[0][1] == board[0][2] == sign or
#         board[1][0] == board[1][1] == board[1][2] == sign or
#         board[2][0] == board[2][1] == board[2][2] == sign or
#         board[0][0] == board[1][0] == board[2][0] == sign or
#         board[0][1] == board[1][1] == board[2][1] == sign or
#         board[0][2] == board[1][2] == board[2][2] == sign or
#         board[0][0] == board[1][1] == board[2][2] == sign or
#         board[0][2] == board[1][1] == board[2][0] == sign):
#         if sign == "X":
#             print("Computer wins!")
#             return True
#         else:
#             print("You win!")
#             return True
        

    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


# def draw_move(board):

#     display_board(board)
#     while True:
#         if make_list_of_free_fields(board):
#             r_move = randrange(1, 10)
#             print("Random move:", r_move)

#             for row in range(len(board)):
#                 for col in range(len(board[row])):
#                     if board[row][col] == r_move:
#                         board[row][col] = "X"
#                         if victory_for(board, "X"):
#                             print("its suppose to break here")
#                             return False
#                         else:
#                             enter_move(board)
#             else:
#                 print("Input already taken. Please choose another move.")
#                 draw_move(board)
#         else:
#             print("It's a tie!")
    
        
  


    
    # The function draws the computer's move and updates the board.

while True:

    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

    if enter_move(board):
        break

    # if draw_move(board):
    #     break

    # if not make_list_of_free_fields(board):
    #     print("It's a tie!")
    #     break


import time


player_1 = None
#player_1 = "o"
player_2 = None
#layer_2 = "x"

while player_1 != "x" and player_1 != 'o' :
    player_1 = input("Player one, select X or O ?")
    if player_1 == "x":
        player_2 = "o"
    else:
        player_2 = "x"    

print(f'Player 1 selected "{player_1}" and Player is "{player_2}" ')
time.sleep(2)


board = ['#'," "," "," "," "," "," "," "," "," "]



def board_game(board):
    print('\n'*100)
    print("TIC TAC TOE")
    print(board[1] + " | " + board[2] + " | "  + board[3])
    print("-"*10)  
    print(board[4] + " | " + board[5] + " | "  + board[6])  
    print("-"*10)  
    print(board[7] + " | " + board[8] + " | "  + board[9])  
    

#print(board)
board_game(board)
choose = input("Player_1 choose (1 - 9) ?")
board[int(choose)] = player_1
board_game(board)

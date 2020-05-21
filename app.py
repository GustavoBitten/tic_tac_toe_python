
import time


player_1 = None
player_1 = "o"
player_2 = None
player_2 = "x"


while player_1 != "x" and player_1 != 'o' :
    player_1 = input("Player one, select X or O ?")
    if player_1 == "x":
        player_2 = "o"
    else:
        player_2 = "x"    


print(f'Player 1 selected "{player_1}" and Player 2 is "{player_2}" ')
#time.sleep(2)


board = ['#',"1","2","3","4","5","6","7","8","9"]



def board_game(board):
    #print('\n'*100)
    print("TIC TAC TOE")
    print(board[1] + " | " + board[2] + " | "  + board[3])
    print("-"*10)  
    print(board[4] + " | " + board[5] + " | "  + board[6])  
    print("-"*10)  
    print(board[7] + " | " + board[8] + " | "  + board[9])  
    

#print(board)
def winCheck(board):
    if board[1] == board[2] == board[3] != " " : 
        return str(board[1])

    elif board[4] == board[5] == board[6] != " " :
        return str(board[4]) 

    elif board[7] == board[8] == board[9] != " " :
        return str(board[7])
        
    elif board[1] == board[4] == board[7] != " " :
        return str(board[1])

    elif board[2] == board[5] == board[8] != " " :
        return str(board[2])

    elif board[3] == board[6] == board[9] != " " :
        return str(board[3])

    elif board[1] == board[5] == board[9] != " " :
        return str(board[1])

    elif board[3] == board[5] == board[7] != " " :
        return str(board[3])
    else:
        return False
        
    




#rint(False)
counter = 0

while True:
    #print(winCheck(board))

    
    board_game(board)
    counter += 1 
    print(counter) 
    choose = input("Player_1 choose (1 - 9) ?")
    board[int(choose)] = player_1
    if winCheck(board) != False:
        break 


    board_game(board)
    counter += 1

    if counter >= 10:

        print('Deu velha!!')
        break

    print(counter) 
    choose = input("Player_2 choose (1 - 9) ?")
    board[int(choose)] = player_2
    if winCheck(board) != False:
        break 
    
#print(board_game(board))

if winCheck(board) == "o":
    board_game(board)
    result = "Player_1"
    print(f'O vencedor é {result}')
elif winCheck(board) == "x":
    board_game(board)
    result = "Player_2"
    print(f'O vencedor é {result}')
     




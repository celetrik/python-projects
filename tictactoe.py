

# #help player pick either x or o
# #make sure each player has enough chances to play their turn on the board.
# #display the player turns
# #make sure each player can make a move into any slot on the board.

# #create a board(dict)
# import random
# plainboard = {
#     1:' ', 2:' ', 3:' ',
#     4:' ', 5:' ', 6:' ',
#     7:' ', 8:' ', 9:' '
# }
# #create a function to print out the board
# def printboard(plainboard):
#     print(plainboard[1] +'|' + plainboard[2] + '|' + plainboard[3])
#     print('-+-+-')
#     print(plainboard[4] + '|' + plainboard[5] + '|' + plainboard[6])
#     print('-+-+-')
#     print(plainboard[7] + '|' + plainboard[8] + '|' + plainboard[9])
#     ('_|_|_')
# printboard(plainboard)
# turn = 'X'
# count = 0
# Round = 'O'
# position = input('x take a move: ')
# comp_position = random.randint(1,9)
# def computer_random():
#     comp_position = random.randint(1,9)


# def game_oneplayer():
#     for i in range(10):
        

# game_oneplayer()

# # printboard(board)
# #take players turn

# # first_move = input('who want to take the first move X or O:  ').upper
# # turn= 'X'
# # if first_move == turn :
# #     print('X take a move')
# #     input_move = int(input())
# #     board[input_move]= first_move
# # elif first_move == 'O':
# #     print('O take a move')
# #     input_move = int(input())
# #     board[input_move]= first_move
# # else:
# #     print('none')

# # def game():

# #     turn = 'X'
# #     count = 0
    
# #     for i in range(10):
# #             printboard(board)
# #             print("It's your turn," + turn + ".Move to which place?")

# #             move = input()        

# #             if board[move] == ' ':
# #                 board[move] = turn
# #                 count += 1
# #             else:
# #                 print("That place is already filled.\nMove to which place?")
# #                 continue
# theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
#             '4': ' ' , '5': ' ' , '6': ' ' ,
#             '1': ' ' , '2': ' ' , '3': ' ' }

# board_keys = []

# for key in theBoard:
#     board_keys.append(key)

# ''' We will have to print the updated board after every move in the game and 
#     thus we will make a function in which we'll define the printBoard function
#     so that we can easily print the board everytime by calling this function. '''

# def printBoard(board):
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])

# # Now we'll write the main function which has all the gameplay functionality.
# def game():

#     turn = 'X'
#     count = 0


#     for i in range(10):
#         printBoard(theBoard)
#         print("It's your turn," + turn + ".Move to which place?")

#         move = input()        

#         if theBoard[move] == ' ':
#             theBoard[move] = turn
#             count += 1
#         else:
#             print("That place is already filled.\nMove to which place?")
#             continue

#         # Now we will check if player X or O has won,for every move after 5 moves. 
#         if count >= 5:
#             if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")                
#                 break
#             elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break 
#             elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break
#             elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
#                 printBoard(theBoard)
#                 print("\nGame Over.\n")                
#                 print(" **** " +turn + " won. ****")
#                 break 

#         # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
#         if count == 9:
#             print("\nGame Over.\n")                
#             print("It's a Tie!!")

#         # Now we have to change the player after every move.
#         if turn =='X':
#             turn = 'O'
#         else:
#             turn = 'X'        
    
#     # Now we will ask if player wants to restart the game or not.
#     restart = input("Do want to play Again?(y/n)")
#     if restart == "y" or restart == "Y":  
#         for key in board_keys:
#             theBoard[key] = " "

#         game()

# if __name__ == "__main__":
#     game()




plainboard =   {'1': ' ', '2': ' ', '3': ' ', 
                '4': ' ', '5': ' ', '6': ' ',
                '7': ' ', '8': ' ', '9': ' '}

board_keys= []

for key in plainboard:
    board_keys.append(key)

def printBoard(plainboard):
    print(plainboard['1'] +'|' + plainboard['2'] + '|' + plainboard['3'])
    print('-+-+-')
    print(plainboard['4'] + '|' + plainboard['5'] + '|' + plainboard['6'])
    print('-+-+-')
    print(plainboard['7'] + '|' + plainboard['8'] + '|' + plainboard['9'])
    
def game():
    
    turn='X'
    count= 0
    for i in range(10):
        printBoard(plainboard)
        print('take a move  '  + turn )
        move=input()
        if plainboard[move]== ' ':
            plainboard[move]=turn
            count+=1
        else:
            print('it has already been filled')
            continue
        if count>= 5:
            if plainboard['1']==plainboard['2']==plainboard['3']!=' ':
                printBoard(plainboard)
                print('\n Game over\n')
                print('****  ' + turn +'  Won. *****')
                break
            elif plainboard['4']==plainboard['5']==plainboard['6']!=' ':
                printBoard(plainboard)
                print('\n Game over\n')
                print('****  ' + turn +'  Won. *****')
                break
            elif plainboard['7']==plainboard['8']==plainboard['9']!=' ':
                printBoard(plainboard)
                print('\n Game over\n')
                print('****  ' + turn +' Won. *****')
                break
            elif plainboard['1']==plainboard['5']==plainboard['9']!=' ':
                printBoard(plainboard)
                print('\n Game over\n')
                print('****  ' + turn +'  Won. *****')
                break
            elif plainboard['3']==plainboard['6']==plainboard['9']!=' ':
                printBoard(plainboard)
                print('\n Game over\n')
                print('****  ' + turn +'  Won. *****')
                break
            elif plainboard['2']==plainboard['5']==plainboard['8']!=' ':
                printBoard(plainboard)
                print('\n Game over\n')
                print('****  ' + turn +'  Won. *****')
                break
            elif plainboard['1']==plainboard['4']==plainboard['7']!=' ':
                printBoard(plainboard)
                print('\n Game over\n')
                print('****  ' + turn +'  Won. *****')
                break
        if count==9:
            print('\n Game over\n')
            print("it's s Tie!!")
        if turn=='X':
            turn='O'
        else:
            turn='X'
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            plainboard[key] = " "
            game()
    else:
        print('Thanks for playing')







game()
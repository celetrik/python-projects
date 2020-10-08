#paper v rock -paper
#rock v scissors - rock
#scissors v paper -scissors


#play against computer - pick at random


#display what the computer chose
#display the current state of wins and losses

#the game should be played repeatedly until the player wants to quit


import sys
import random



print('ROCK PAPER SCISSORS')

# record wins, losses and ties
wins = 0
loss = 0
ties = 0



while True:
    print(f"{wins} wins, {loss} losses, {ties} ties")
    while True:
        #give the player an way to play their move or quit the game.
        players_move = input('take a move input: P or R or S or Q to quit')

        if players_move.upper() == 'Q':
            print('game ended')
            sys.exit()
        if players_move == 'R' or players_move == 'S' or players_move == 'P':
            break
        print('you can enter P, R or Q')
        

     # display the player's move
    if players_move == 'R':
        print('Rock versus...')
    elif players_move == 'P':
        print('Paper versus...')
    elif players_move == 'S':
        print('Scissors versus...')


    random_int = random.randint(1, 3)

    if random_int == 1:
        computer_move = 'P'
        print('Paper')
    elif random_int == 2:
        computer_move = 'R'
        print('Rock')
    elif random_int == 3:
        computer_move = 'S'
        print('Scissors')


    #compare the moves with each other and update the scores
    if players_move == computer_move:
        print('it\'s a tie')
        ties += 1
    elif players_move == 'P' and computer_move == 'R':
        print('You win!')
        wins += 1
    elif players_move == 'S' and computer_move == 'P':
        print('You win!')
        wins += 1
    elif players_move == 'R' and computer_move == 'S':
        print('You win!')
        wins+=1
    elif players_move == 'P' and computer_move == 'S':
        print('You lost')
        loss+=1
    elif players_move == 'S' and computer_move == 'R':
        print('You lost')
        loss+=1
    elif players_move == 'R' and computer_move == 'P':
        print('You lost')
        loss+=1

















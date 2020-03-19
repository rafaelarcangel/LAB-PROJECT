board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

player = "x"
result = True


def show_matrix():
    print(board[0], '|', board[1], '|', board[2])
    print ('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[6], '|', board[7], '|', board[8])
    print('\r\n')


def check_tictaktoelogic():
    ##Check if any horizantal rows are done
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        print (player + ' Won! Congrats!!!!')
        return False
    ##Check if any vertical column are done
    if board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        print (player + ' Won! Congrats!!!!')
        return False
    ## check if any diagonals are done
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        print (player + ' Won! Congrats!!!!')
        return False
        ## Check for match  draw
    if board[0] == 0 or board[1] == 1 or board[2] == 2 or board[3] == 3 or board[4] == 4 or board[5] == 5 or board[
        6] == 6 or board[7] == 7 or board[8] == 8:
        return True
    else:
        print ('Oops, game is a draw... Try Again?')
        return False
    return True

while result:
    show_matrix()
    print ('Enter for player ' + player)
    index = int(input("Select a Spot: "))
    if index >= 0 or index <= 8:

        if board[index] != 'x' and board[index] != 'o':
            board[index] = player
        else:
            print ('This spot is taken!')
        result = check_tictaktoelogic()
        if player == "x":
            player = "o"
        else:
            player = "x"
from functions.py import *
count = 0  
board = createBoard()
printBoard(board)
player = 'X'
while True:
    move = input( 'player'+player+' (col #): ')
    if move == 'e': 
        break
    try:
        b = makeMove(board, player, int(move))
    except:
        printBoard(board)
        continue
    printBoard(board)
    if b == 0:
        break
    elif b == 1:
        continue
    count += 1
    result = checkWin(board, player, int(move), globalrow)
    if result == None:
        if count == len(board) * len(board[0]):
            print('Draw!')
            break
    else:
        print(result)
        break
    if player == 'X': player = 'O'
    else: player = 'X'
print('bye')
def createBoard():
    r, c = 6, 7
    if 'n' == input('Standard game? (y/n): '):
        r, c = int(input('r? (2 - 20): ')), int(input('c? (2 - 20): '))
    return [['·'] * c for i in range(r)]

def printBoard(board):
    r, c = len(board), len(board[0])
    spaces = 1
    if r>9 or c>9: spaces = 2 #bigBoard
    x = ''
    for row in range(r-1,-1, -1):
        x += f'{row:>{spaces}}'
        ss = ' '
        if spaces==2: ss = ' '
        for col in range(c):
            x += ss+board[row][col]
        x += ' \n'
    x += ' ' + ' '*spaces
    for col in range(c): x += f'{col:>{spaces}}'+' '
    print(x)
def makeMove(board, player, col):
    global globalrow
    r = len(board)
    if col == 'e':
        return 0
    for row in range(r):
        try:
            if board[row][col]!='·' and board[row+1][col]=='·':
                board[row+1][col] = player
                globalrow = row + 1
                break
            elif board[row][col]=='·':
                board[row][col] = player
                globalrow = row
                break
        except:
            return 1
def checkWin(board, player, col,globalrow):
    temp = [[] for i in range(4)]
    for i in range(len(board)):
        if board[i][col] == player:
            temp[0].append(i)
    for i in range(len(board[0])):
        if board[globalrow][i] == player:
            temp[1].append(i)
    r1 = globalrow
    c1 = col
    while True:
        if r1 - 1 >= 0 and c1 - 1 >= 0:
            r1 -= 1
            c1 -= 1
        else: break
    while True:
        if board[r1][c1] == player:
            temp[2].append(r1) 
        if r1 != len(board)-1 and c1 != len(board[0])-1:
            r1 += 1
            c1 += 1
        else:
            break
    r1 = globalrow
    c1 = col
    while True:
        if r1 - 1 >= 0 and c1 + 1 <= len(board[0])-1:
            r1 -= 1
            c1 += 1
        else:   break
    while True:   
        if board[r1][c1] == player:
            temp[3].append(r1) 
        if r1 + 1 < len(board)-1 and c1 - 1 > 0:
            r1 += 1
            c1 -= 1
        else:
            break

    for i in temp:
        if len(i) == 4:
            if sorted(i) == [*range(sorted(i)[0],sorted(i)[-1]+1)]:
                return (f'Player {player} has won!')
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
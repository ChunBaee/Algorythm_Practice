def setWay(n):
    value = list()
    for i in range(n-1, 0, -1):
        value.append(i)
        value.append(i)
    return value

def plusY(o, board):
    global numb
    global cursorX
    global cursorY
    for i in range(0 ,o):
        cursorY += 1
        numb += 1
        board[cursorX][cursorY] = numb




def plusX(o, board):
    global numb
    global cursorX
    global cursorY
    for i in range(0 ,o):
        cursorX += 1
        numb += 1
        board[cursorX][cursorY] = numb




def minusY(o,  board):
    global numb
    global cursorX
    global cursorY
    for i in range(0 ,o):
        cursorY -= 1
        numb += 1
        board[cursorX][cursorY] = numb



def minusX(o, board):
    global numb
    global cursorX
    global cursorY
    for i in range(0 ,o):
        cursorX -= 1
        numb += 1
        board[cursorX][cursorY] = numb




T = int(input())

for i in range(1, T + 1):
    n = int(input())

    board = [[0 for _ in range(0, n)] for _ in range(0, n)]

    way = [n-1]
    way += setWay(n)

    print(way)

    numb = 1
    turn = 0
    cursorX = 0
    cursorY = 0
    board[0][0] = 1
    for o in way:
        if turn == 0:
            plusY(o, board)
        elif turn == 1:
            plusX(o, board)
        elif turn == 2:
            minusY(o, board)
        elif turn == 3:
            minusX(o, board)
        turn += 1
        turn %= 4
    print(board)


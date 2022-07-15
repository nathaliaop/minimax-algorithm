INF = 1e9+17
FIRSTPLAYER = 'X'
SECONDPLAYER = 'O'

def isBoardFull(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                return False
    return True

def playerWins(board, player):
    # win on either diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    for i in range(3):
        # win on row
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
            return True
        # win on column
        if (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    return False

def boardValue(board):
    if playerWins(board, FIRSTPLAYER):
        return 1
    elif playerWins(board, SECONDPLAYER):
        return -1
    else:
        return 0

def generatePossibleBoards(board, player):
    possibleBoards = []
    auxBoard = board
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                auxBoard[i][j] = player
                possibleBoards.append(auxBoard)
                auxBoard = board
    return possibleBoards

def minimax(board, depth, player):
    if depth == 0 or isBoardFull(board):
        return boardValue(board)
    if player == FIRSTPLAYER:
        value = -INF
        for child in generatePossibleBoards(board, player):
            value = max(value, minimax(child, depth - 1, SECONDPLAYER))
        return value
    else:
        value = INF
        for child in generatePossibleBoards(board, player):
            value = min( value, minimax( child, depth - 1, FIRSTPLAYER))
        return value

if __name__ == '__main__':
    board = [['O', 'X', ' '], ['X', ' ', ' '], ['X', 'O', 'O']]
    initialPlayer = 'X'
    depth = 3
    print(minimax(board, depth, initialPlayer))
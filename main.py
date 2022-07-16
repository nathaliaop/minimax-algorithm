import copy

INF = 1e9+17
dp = {}

def isBoardFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
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
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        # win on column
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False


def boardValue(board, cpu, user):
    if playerWins(board, cpu):
        return 1
    elif playerWins(board, user):
        return -1
    else:
        return 0


def generatePossibleBoards(board, player):
    possibleBoards = []
    auxBoard = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                auxBoard[i][j] = player
                possibleBoards.append(auxBoard)
                auxBoard = copy.deepcopy(board)
    return possibleBoards

def createHash(board):
    ans = ''

    for i in range(3):
        for j in range(3):
            ans += board[i][j]

    return ans

def minimax(board, depth, player, cpu, user):
    global dp
    myhash = createHash(board)

    try:
        ans = dp[myhash]

        return ans
    except:
        pass

    if depth == 0 or isBoardFull(board) or playerWins(board, cpu) or playerWins(board, user):
        dp[myhash] = boardValue(board, cpu, user)
        return dp[myhash]
    if player == cpu:
        value = -INF
        for child in generatePossibleBoards(board, player):
            value = max(value, minimax(child, depth - 1, user, cpu, user))
        dp[myhash] = value
        return value
    else:
        value = INF
        for child in generatePossibleBoards(board, player):
            value = min(value, minimax(child, depth - 1, cpu, cpu, user))
        dp[myhash] = value
        return value


def calculateDepth(board):
    depth = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                depth += 1
    return depth


def bestMove(board, cpu, user):
    if isBoardFull(board):
        return board
    possibleBoards = generatePossibleBoards(board, cpu)
    curr = -INF
    best_move = []
    depth = calculateDepth(possibleBoards[0])
    for possibleBoard in possibleBoards:
        minimaxResult = minimax(possibleBoard, depth, user, cpu, user)
        if minimaxResult > curr:
            curr = minimaxResult
            best_move = possibleBoard

    return best_move

def choosePlayers():
    cpu = "X"
    print("Choose X or O")
    user = input()

    while user.upper() != "X" and user.upper() != "O":
        print("Choose X or O")
        user = input()

    user = user.upper()
    cpu = cpu.upper()

    if user == "X":
        cpu = "O"

    return (cpu, user)

# dictonary that associates a number from 1 to 8 to a position in the board matriz
def defineBoardPositions():
    positions = {}
    it = 0
    for i in range(3):
        for j in range(3):
            positions[it] = (i,j)
            it += 1

    return positions

def showBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], " | ", end="")
        print("\n")
    
    return None

def showResult(board, cpu, user):
    showBoard(board)
    result = boardValue(board, cpu, user)
    match result:
        case 0:
            print("It's a draw")
        case 1:
            print("CPU won")
        case -1:
            print("You won")

    return None

def main():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    possibleMoves = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    positions = defineBoardPositions()
    cpu, user = choosePlayers()

    while (
        not isBoardFull(board)
        and not playerWins(board, user)
        and not playerWins(board, cpu)
    ):
        print("Make a move")
        showBoard([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        showBoard(board)
        move = input()
        # if move is valid and not yet occupied
        while move not in possibleMoves or (move in possibleMoves and board[positions[int(move)][0]][positions[int(move)][1]] != ' '):
            print("Make a valid move")
            showBoard([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
            showBoard(board)
            move = input()
        move = int(move)
        # user move
        board[positions[move][0]][positions[move][1]] = user
        # cpu move
        board = bestMove(board, cpu, user)
        print("------------------------")

    showResult(board, cpu, user)


if __name__ == "__main__":
    main()
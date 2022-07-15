INF = 1e9+17
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def boardValue(board):
    pass
    
def generatePossibleBoard(board, maximizingPlayer):
    pass

def minimax( board, depth, maximizingPlayer):
    if depth == 0 or idBoardFull(board)#node is a terminal node then
        return boardValue(board)# the heuristic value of node
    if maximizingPlayer:
        value = −INF
        for child in generatePossibleBoard(board, maximizingPlayer):#each child of node do
            value = max(value, minimax(child, depth − 1, FALSE))
        return value
    else: #(* minimizing player *)
        value = INF
        for each child in generatePossibleBoard(board, maximizingPlayer): #of node do
            value = min( value, minimax( child, depth − 1, TRUE ) )
        return value

print(minimax(board, depth, TRUE))
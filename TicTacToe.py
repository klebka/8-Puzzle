def start():
    board = [ #0,0 -> 2,2
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    turn = 0
    play(board, turn)

def play(board, turn): #game loop
    print(">Tic Tac Toe<\n"
          "-------------")
    turn = 0
    while(turn<9):
        while(True):
            if(turn %2 == 0): move = input("Player 1(row,column): ")
            else: move = input("Player 2(row,column): ")
            try:
                row = int(move[0]); col = int(move[2])
            except:
                continue
            if(row not in [0,1,2] or col not in [0,1,2]): continue #within board
            break
        validity = updateBoard(board, row, col, turn)
        if validity == 0: continue #try another move
        turn +=1
        displayBoard(board)
        if(turn>4): solve(board)

def updateBoard(board, row, col, turn):
    if(board[row][col] == " "):
        if(turn %2 == 0): 
            board[row][col] = "x"
            return 1 #valid move
        else:
            board[row][col] = "o"
            return 1
    else: 
        return 0 #invalid move
    
def displayBoard(board):
    rowCtr = 0
    while(rowCtr < 3):
        colCtr = 0
        print("|", end = "")
        while(colCtr < 3):
            print(board[rowCtr][colCtr], end = "|")
            colCtr +=1
        print()
        rowCtr +=1

def solve(board): #check for winner
    #row cases
    rowCtr = 0
    while(rowCtr < 3):
        colCtr = 0
        if(board[rowCtr][colCtr] != " "):
            if(board[rowCtr][colCtr] == board[rowCtr][colCtr +1] and board[rowCtr][colCtr +1] == board[rowCtr][colCtr +2]):
                if(board[rowCtr][colCtr] == "x"): finish(1)
                else: finish(2)
        rowCtr +=1
    
    #column cases
    while(colCtr < 3):
        rowCtr = 0
        if(board[rowCtr][colCtr] != " "):
            if(board[rowCtr][colCtr] == board[rowCtr +1][colCtr] and board[rowCtr +1][colCtr] == board[rowCtr +2][colCtr]):
                if(board[rowCtr][colCtr] == "x"): finish(1) #winner found
                else: finish(2)
        colCtr +=1
    
    #2 diagonal cases
    if(board[0][0] != " "):
        if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if(board[0][0] == "x"): finish(1)
            else: finish(2)   
    if(board[0][2] != " "):
        if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            if(board[0][2] == "x"): finish(1)
            else: finish(2)

def finish(player):
    if(player == 1): #player x
        print("Player 1 Won")
        quit()
    else: #player o
        print("Player 2 Won")
        quit()

start()
import random

def start():
    board = [None] * 9 #empty array
    moveCtr = 0
    randomize(board)
    displayBoard(board)
    play(board, moveCtr)

def randomize(board): #board generation
    while(True):
        possible = [1,2,3,4,5,6,7,8,9]
        for block in range(0,9):
            while(True):
                newInt = random.randint(1,9)
                if(newInt not in possible): continue
                possible.remove(newInt) #ensure no duplicate
                break
            board[block] = newInt
        if(isValid(board) == 0): continue
        break

def isValid(board):
    if(invCount(board) %2 == 0): return 1 #solvable
    else: return 0

def invCount(board):
    invCtr = 0
    for block in range(0,9): #this block compared to all blocks
        for nextBlocks in range(block +1, 9):
            if(board[block] != 9 and board[nextBlocks] != 9 and board[block] > board[nextBlocks]):
                invCtr +=1
    return invCtr

def play(board, moveCtr): 
    while(True):
        while(True):
            move = input("Slide empty block(^,v, <, >): ")
            if(move not in ["^", "v", "<", ">"]): 
                print("invalid move")
                continue
            break
        validity = updateBoard(board, move) 
        if(validity == 1):
            moveCtr +=1
            print("Move:", moveCtr, end="")
            displayBoard(board)
            isWon(board, moveCtr)

def updateBoard(board, move):
    for block in range(0,9):
        if(board[block] == 9):
            if(move == "^"): #up
                if(block in [0,1,2]): #invalid pos for move
                   print("invalid move")
                   return 0 #invalid
                board[block -3], board[block] = board[block], board[block -3] #block swap
                break
            if(move == "v"): #down
                if(block in [6,7,8]): 
                   print("invalid move")
                   return 0
                board[block], board[block +3] = board[block +3], board[block]
                break
            if(move == "<"): #left
                if(block in [0,3,6]): 
                   print("invalid move")
                   return 0
                board[block -1], board[block] = board[block], board[block -1]
                break
            if(move == ">"): #right
                if(block in [2,5,8]): 
                   print("invalid move")
                   return 0
                board[block], board[block +1] = board[block +1], board[block]
                break
    return 1 #valid

def displayBoard(board):
    for block in range(0,9):
        if((block +3) %3 == 0): print("\n",end = "|") #every start
        if(board[block] == 9): print(" ", end = "|")
        else: print(board[block], end = "|")
    print() #clean

def isWon(board, moveCtr):
    if(board == [1,2,3,4,5,6,7,8,9]): #board in order
        print("You Won!", "\nTurns taken:", moveCtr); quit()

start()
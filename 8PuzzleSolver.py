import random

def start():
    board = [None] * 9 #empty array
    moveCtr = 0
    #randomizedBoard = randomize(board)
    loadedBoard = load(board)
    displayBoard(loadedBoard)
    solve_bfs(loadedBoard)
    solve_dfs(loadedBoard)

def load(board): #load from specified file
    file = open("input.txt","r")
    toSplit = file.read().splitlines() #split newlines
    board = toSplit[0].split(";") + toSplit[1].split(";") + toSplit[2].split(";") #split lists using ";" then combine lists
    for i in range(0,9):
        board[i] = int(board[i]) #turn all values to int
    file.close()
    if(isValid(board) == 0): 
        displayBoard(board)
        print("Unsolvable Board")
        quit()
    return board

def randomize(board): #board generation
    while(True):
        possible = [0,1,2,3,4,5,6,7,8]
        for block in range(0,9):
            while(True):
                newInt = random.randint(0,8)
                if(newInt not in possible): continue
                possible.remove(newInt) #ensure no duplicate
                break
            board[block] = newInt
        if(isValid(board) == 0): continue #when unsolvable, regenerate
        break
    return board

def isValid(board):
    if(invCount(board) %2 == 0): return 1 #solvable
    else: return 0

def invCount(board):
    invCtr = 0
    for block in range(0,9): #this block compared to all blocks
        for nextBlocks in range(block +1, 9):
            if((board[block] != 0 and board[nextBlocks] != 0 and board[block] > board[nextBlocks])):
                invCtr +=1
    return invCtr

def updateBoard(board, move):
    for block in range(0,9):
        if(board[block] == 0):
            if(move == "w"): #up
                board[block -3], board[block] = board[block], board[block -3] #block swap
                break
            if(move == "s"): #down
                board[block], board[block +3] = board[block +3], board[block]
                break
            if(move == "a"): #left
                board[block -1], board[block] = board[block], board[block -1]
                break
            if(move == "d"): #right
                board[block], board[block +1] = board[block +1], board[block]
                break
    return board

def displayBoard(board):
    for block in range(0,9):
        if((block +3) %3 == 0): print("\n",end = "|") #every start
        if(board[block] == 0): print(" ", end = "|")
        else: print(board[block], end = "|")
    print() #clean

def isWon(board, moveCtr, actionTaken, pathCost):
    if(board == [1,2,3,4,5,6,7,8,0]): #board in order
        displayBoard(board)
        print("Solved", "\nExplored states:", moveCtr); print("Path Cost: ", pathCost); print("Moves Done: ", end = "")
        for action in actionTaken: print(action, end=" ")
        print()
        quit()

def solve_bfs(board):
    frontier = [board]
    explored = []
    actionTaken = []
    while(len(frontier) != 0):
        currentState = frontier.pop(0)
        explored.append(currentState)
        isWon(currentState,len(explored), actionTakenHelper(actionTaken), len(actionTaken)) #check if solved
        actions = possibleActions(currentState) #check for possible actions
        for action in actions:
            holderState = currentState.copy() #always copy original current state
            tempState = updateBoard(holderState, action) #only update the copy of original
            if(tempState not in explored and tempState not in frontier and tempState != 0): #check if not explored or to be explored
                frontier.append(tempState)
    print("explored all")
    
def solve_dfs(board):
    frontier = [board]
    explored = []
    actionTaken = []
    while(len(frontier) != 0):
        currentState = frontier.pop(-1)
        explored.append(currentState)
        isWon(currentState,len(explored), actionTakenHelper(actionTaken), len(actionTaken)) #check if solved
        actions = possibleActions(currentState) #check for possible actions
        for action in actions:
            holderState = currentState.copy() #always copy original current state
            tempState = updateBoard(holderState, action) #only update the copy of original
            if(tempState not in explored and tempState != 0): #check if not explored or to be explored
                frontier.append(tempState)
    print("explored all")
    
def possibleActions(board):
    for block in range(0,9):
        if(board[block] == 0):
            if(block in [0]): return ["d","s"] #corners
            elif(block in [2]): return ["s","a"]
            elif(block in [6]): return ["w","d"]
            elif(block in [8]): return ["w","a"]
            elif(block in [0,1,2]): return ["d","s","a"] #sides
            elif(block in [6,7,8]): return ["w","d","a"]
            elif(block in [0,3,6]): return ["w","d","s"]
            elif(block in [2,5,8]): return ["w","s","a"]
            elif(block in [4]): return ["w","d","s","a"] #center
            
def actionTakenHelper(actionTaken):
    actualAction = []
    for action in actionTaken: #format
        if(action == "w"): actualAction.append("U") #reversed from bottom-up
        elif(action == "d"): actualAction.append("R")
        elif(action == "s"): actualAction.append("D")
        elif(action == "a"): actualAction.append("L")
    return actualAction

start()

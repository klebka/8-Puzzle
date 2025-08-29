import random

def start():
    board = [None] * 9 #empty array
    menu(board)

def menu(board):
    while(True):
        print("[1] Generate Random Board")
        print("[2] Load from Input.txt")
        choice = input("Select mode: ")
        if(choice == "1"):
            board = randomize(board)
            solverMenu(board)
        elif(choice == "2"):
            board = load(board)
            solverMenu(board)
        elif(choice == "3"):
            quit()
        else: print("invalid selection")

def solverMenu(board):
    displayBoard(board)
    while(True):
        print("[1] Solve with BFS")
        print("[2] Solve with DFS")
        choice = input("Select mode: ")
        if(choice == "1"):
            solve_bfs(board)
            return
        elif(choice == "2"):
            solve_dfs(board)
            return
        elif(choice == "3"):
            return
        else: print("invalid selection")


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
        return 1

def solve_bfs(board):
    frontier = [board]
    explored = []
    path = []
    while(len(frontier) != 0):
        currentState = frontier.pop(0)
        if(len(currentState) == 10):
            path = currentState.pop()
        explored.append(currentState)
        if(isWon(currentState,len(explored), actionTakenHelper(path), len(path)) == 1): return #check if solved
        actions = possibleActions(currentState) #check for possible actions
        for action in actions:
            tempState = currentState.copy() #always copy original current state
            updateBoard(tempState, action) #only update the copy of original
            if(tempState in explored):
                path.append(action)
            if(tempState not in explored and tempState not in frontier and tempState != 0): #check if not explored or to be explored
                tempState.append(path)
                frontier.append(tempState)
    print("explored all")
    
def solve_dfs(board):
    frontier = [board]
    explored = []
    path = []
    while(len(frontier) != 0):
        currentState = frontier.pop()
        if(len(currentState) == 10):
            path = currentState.pop()
        explored.append(currentState)
        if(isWon(currentState,len(explored), actionTakenHelper(path), len(path)) == 1): return #check if solved
        actions = possibleActions(currentState) #check for possible actions
        for action in actions:
            tempState = currentState.copy() #always copy original current state
            updateBoard(tempState, action) #only update the copy of original
            if(tempState in explored):
                path.append(action)
            if(tempState not in explored and tempState != 0): #check if not explored
                tempState.append(path)
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

import random

#Working:
#test case 1: H1 H2
#test case 1: H1 H2
#test case 1: H1 H2
#test case 1: H2

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
        elif(choice == "0"):
            quit()
        else: print("invalid selection")

def solverMenu(board):
    displayBoard(board)
    while(True):
        print("[1] Solve with BFS")
        print("[2] Solve with DFS")
        print("[3] Solve with A*")
        choice = input("Select mode: ")
        if(choice == "1"):
            solve_bfs(board)
            return
        elif(choice == "2"):
            solve_dfs(board)
            return
        elif(choice == "3"):
            print("Solve based on:")
            print("[1] Misplaced tiles")
            print("[2] Manhattan Distance")
            #print("[3] Non-adjacent tiles")
            choice = input("Select mode: ")
            if(choice == "1"):
                heuristic = 1
            elif(choice == "2"):
                heuristic = 2
            elif(choice == "3"):
                #heuristic = 3
                print("not implemented yet")
                break
            elif(choice == "0"):
                continue
            solve_astar(board, heuristic)
            return
        elif(choice == "0"):
            return
        else: print("invalid selection")

def load(board): #load from specified file
    file = open("input.txt","r")
    toSplit = file.read().splitlines() #split newlines
    if(len(toSplit) == 0): print("Empty Board"); quit()
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
    if(board[0:9] == [1,2,3,4,5,6,7,8,0]): #board in order
        displayBoard(board)
        print("Solved", "\nPath Cost: ", pathCost, "\nExplored states:", moveCtr, "\nMoves Done: ", end = "")
        for action in actionTaken: print(action, end=" ")
        print()
        return 1
    return 0

def solve_bfs(board):
    frontier = [board]
    explored = []
    path = []
    while(len(frontier) != 0):
        print("solving: ", len(explored))
        currentState = frontier.pop(0) #FiFo
        if(len(currentState) == 10): #only when has track
            path = currentState.pop() #remove the track of actions
        explored.append(currentState)
        if(isWon(currentState,len(explored), actionTakenHelper(path), len(path)) == 1): return #check if solved
        actions = possibleActions(currentState) #check for possible actions
        for action in actions:
            tempPath = path.copy() #copy path to prevent modification
            tempState = currentState.copy() #copy original current state to prevent modification
            updateBoard(tempState, action) #only update the copy of original
            tempPath.append(action) #keep track of actions
            if(tempState not in explored and tempState not in frontier and tempState != 0): #check if not explored or to be explored
                tempState.append(tempPath) #add track
                frontier.append(tempState)
    print("explored all")
    
def solve_dfs(board):
    frontier = [board]
    explored = []
    path = []
    while(len(frontier) != 0):
        currentState = frontier.pop() #FiLo
        if(len(currentState) == 10):
            path = currentState.pop()
        explored.append(currentState)
        if(isWon(currentState,len(explored), actionTakenHelper(path), len(path)) == 1): return
        actions = possibleActions(currentState)
        for action in actions:
            tempPath = path.copy()
            tempState = currentState.copy()
            updateBoard(tempState, action)
            tempPath.append(action)
            if(tempState not in explored and tempState != 0): #check only if not explored
                tempState.append(tempPath)
                frontier.append(tempState)

    print("explored all")
    
def solve_astar(board, heuristic):
    frontier = [board] #[b,o,a,r,d, [path], f(n)]
    explored = []
    path = []
    while(len(frontier) != 0):
        print("solving: ", len(explored))
        counter = 0
        bestState = frontier.pop()
        if(len(bestState) > 9): #only if [path] and f(n) is present
            for state in frontier:
                if(state[10] < bestState[10]): #finding best f(n)
                    bestState = state.copy()
                    frontier.pop(counter)
                    break
                counter += 1 #track index
            path = bestState.pop(9) #remove the track of actions
        explored.append(bestState)
        if(isWon(bestState,len(explored), actionTakenHelper(path), len(path)) == 1): return #check if solved
        actions = possibleActions(bestState)
        for action in actions:
            tempPath = path.copy()
            tempState = bestState.copy()
            updateBoard(tempState, action)
            tempPath.append(action)
            if((tempState not in explored and tempState not in frontier) or (tempState in explored and duplicateCheck(explored, tempState) == 1)): #check if not explored or to be explored OR if in explored but has lower f(n)
                if(len(tempState) == 10): tempState.pop() #remove f(n) to recalculate
                tempState.append(tempPath)
                if(heuristic == 1): #for misplaced tiles
                    tempState.append(countMisplaced(tempState) + len(tempPath)) #f(n) = h(n) + g(n)
                if(heuristic == 2): #for manhattan
                    tempState.append(manhattan(tempState) + len(tempPath))
                frontier.append(tempState)
    print("explored all")

def duplicateCheck(explored, stateToCompare):
    counter = 0
    for state in explored:
        if(state[0:9] == stateToCompare[0:9] and stateToCompare[-1] <= state[-1]): #check if same state then check if lower f(n)
            explored.pop(counter) #delete duplicate
            return 1
        counter += 1
    return 0

def countMisplaced(board):
    misplaced = 0
    for block in range(0,8):
        if(board[block] != block+1 and board[block] != 0): misplaced += 1 #check if block at 0th Position is 1 (Nth Position == N+)
    if(board[8] != 0): misplaced += 1 #for 9th block
    return misplaced

def manhattan(board):
    distance = 0
    goalState = [1,2,3,4,5,6,7,8,0]
    for block in range(0,8):
        if(board[block] != block+1 and board[block] != 0): #if misplaced
            x,y = translateIndex(goalState.index(board[block])) #translate index to coordinate
            a,b = translateIndex(block)
            distance += (abs(x-a) + abs(y-b)) #|x1-x2| + |y1-y2|
    if(board[8] != 0): #for 9th block
        x,y = translateIndex(goalState.index(board[block]))
        a,b = translateIndex(block)
        distance += (abs(x-a) + abs(y-b))
    return distance

def translateIndex(index):
    if(index == 0): return 0,0 #0,0 0,1 0,2
    if(index == 1): return 0,1 #1,0 1,1 1,2
    if(index == 2): return 0,2 #2,0 2,1 2,2
    if(index == 3): return 1,0
    if(index == 4): return 1,1
    if(index == 5): return 1,2
    if(index == 6): return 2,0
    if(index == 7): return 2,1
    if(index == 8): return 2,2

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

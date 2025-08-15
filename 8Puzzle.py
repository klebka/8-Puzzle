import random

def start():
    board = [ #0,0 -> 2,2
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    moveCtr = 0
    randomize(board)
    start(board)

def randomize(board):
    possible = [1,2,3,4,5,6,7,8,9]
    rowCtr = 0
    while(rowCtr < 3):
        colCtr = 0
        while(colCtr < 3):
            while(True):
                newInt = random.randint(1,9)
                if(newInt not in possible): continue
                possible.remove(newInt)
                break
            if(newInt == 9): board[rowCtr][colCtr] = " "
            else: board[rowCtr][colCtr] = newInt
            colCtr +=1
        rowCtr +=1
    displayBoard(board)

def play(board): 
    while(True):
        while(True):
            move = input("Slide empty block(^,v, <, >)")
            if(move not in ["^", "v", "<", ">"]): continue
            break
        updateBoard(board)

def updateBoard(board):
   print

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

start()
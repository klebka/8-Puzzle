import random

def start():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    turn = 0
    play(board, turn)

def play(board, turn):
    print(">Tic Tac Toe<\n"
          "-------------")
    turn = 0
    while(turn<=9):
        move = input("Player Move(row,column): ")
        row = move[0]; column = move[1]
        updateBoard(board, row, column, turn)

def updateBoard(board, row, column, turn):
    if(board[row,column] == " "):
        if(turn %2 == 0): 
            board[row,column] = "x"
        else:
            board[row, column] = "o"
    else:
        return 0 #invalid move
    
    while(True):
        print[board[row,column]]

def solve():
    print


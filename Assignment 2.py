# Tic-Tac-Toe Program using
# random number in Python

# importing all necessary libraries
import numpy as np
import random
from time import sleep

# Creates an empty board
def create_board():
     return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
 
    
    # Check for empty places on board
def possibilities(board):
     l = []
     
     for i in range(len(board)):
        for j in range(len(board)):
              
            if board[i][j] == 0:
                l.append((i, j))
     return(l)

# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return(board)

# Checks whether the player has three 
# of their marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        win = True
          
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
                  
        if win == True:
            return(win)
    return(win)

# Checks whether the player has three
# of their marks in a vertical row

def col_win(board, player):
    for x in range(len(board)):
        win = True
          
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
                  
        if win == True:
            return(win)
    return(win)

# Checks whether the player has three
# of their marks in a diagonal row

def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win

# Evaluates whether there is
# a winner or a tie 

def evaluate(board):
    winner = 0
      
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board,player) or 
            diag_win(board,player)):
                 
            winner = player
              
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# Main function to start the game

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)
      
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return(winner)

# Driver Code
print("Winner is: " + str(play_game()))




# importing libraries
import cv2
import numpy as np
   
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('tree.mp4')
   
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
while(cap.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
   
    # Display the resulting frame
    cv2.imshow('Frame', frame)
   
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()

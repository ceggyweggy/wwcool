'''
TIC TAC TOE PLUS: 9*9 GRID 
... ... ...     1. win small grids by winning 3 in row 
... ... ...     2. win large grids by winning 3 small 
... ... ...        grids in a row

... ... ...     3. move in small grid directs next move 
... ..M .N.     (M for current move, N for centre of new
... ... ...     grid) (can put anywhere in grid N)

... ... ...     4. once square is won/completely filled,
... ... ...     any move directed towards that square 
... ... ...     will allow next player to put in any sq
'''

import math 

class tictactoe():
  def __init__(self):
    rows, cols = (9, 9)
    self.board = [['.']*rows for _ in range(cols)]
    self.won = [[' ']*3 for _ in range(3)]
    self.turn = 'X'
    self.xcor = -1 
    self.ycor = -1 
    self.message = ''
    self.game_ended = False
    self.anywhere = False 

  def check_square(self, x, y):
    square_x = math.floor(x/3)
    square_y = math.floor(y/3)
    if square_x == self.xcor and square_y == self.ycor:
      return True
    return False 

  def check_small_win(self, x, y):
    square_x = math.floor(x/3)
    square_y = math.floor(y/3)
    # 1
    # ONN
    # ONN
    # ONN
    if self.board[square_x*3][square_y*3] == self.board[square_x*3+1][square_y*3] == self.board[square_x*3+2][square_y*3] != '.':
      return self.board[square_x*3][square_y*3]
    # 2
    # OOO
    # NNN 
    # NNN 
    if self.board[square_x*3][square_y*3] == self.board[square_x*3][square_y*3+1] == self.board[square_x*3][square_y*3+2] != '.':
      return self.board[square_x*3][square_y*3]
    # 3
    # ONN
    # NON
    # NNO
    if self.board[square_x*3][square_y*3] == self.board[square_x*3+1][square_y*3+1] == self.board[square_x*3+2][square_y*3+2] != '.':
      return self.board[square_x*3][square_y*3]
    # 4
    # NNO
    # NON 
    # ONN
    if self.board[square_x*3+2][square_y*3] == self.board[square_x*3+1][square_y*3+1] == self.board[square_x*3][square_y*3+2] != '.':
      return self.board[square_x*3+2][square_y*3]
    # 5
    # NON
    # NON 
    # NON
    if self.board[square_x*3][square_y*3+1] == self.board[square_x*3+1][square_y*3+1] == self.board[square_x*3+2][square_y*3+1] != '.':
      return self.board[square_x*3][square_y*3+1]
    # 6
    # NNO
    # NNO 
    # NNO
    if self.board[square_x*3][square_y*3+2] == self.board[square_x*3+1][square_y*3+2] == self.board[square_x*3+2][square_y*3+2] != '.':
      return self.board[square_x*3][square_y*3+2]
    # 7
    # NNN
    # OOO 
    # NNN
    if self.board[square_x*3+1][square_y*3] == self.board[square_x*3+1][square_y*3+1] == self.board[square_x*3+1][square_y*3+2] != '.':
      return self.board[square_x*3+1][square_y*3]
    # 8
    # NNN
    # NNN 
    # OOO
    if self.board[square_x*3+2][square_y*3] == self.board[square_x*3+2][square_y*3+1] == self.board[square_x*3+2][square_y*3+2] != '.':
      return self.board[square_x*3+2][square_y*3]
    return 'N'

  def check_big_win(self):
    if self.won[0][0] == self.won[1][0] == self.won[2][0] != ' ':
      return self.won[0][0]
    if self.won[0][0] == self.won[0][1] == self.won[0][2] != ' ':
      return self.won[0][0]
    if self.won[0][0] == self.won[1][1] == self.won [2][2] != ' ':
      return self.won[0][0];
    if self.won[1][0] == self.won[1][1] == self.won[1][2] != ' ':
      return self.won[1][0]
    if self.won[2][0] == self.won[2][1] == self.won[2][2] != ' ':
      return self.won[2][0]
    if self.won[0][1] == self.won[1][1] == self.won[2][1] != ' ':
      return self.won[0][1] 
    if self.won[0][2] == self.won[1][2] == self.won[2][2] != ' ':
      return self.won[2][2]
    if self.won[0][2] == self.won[1][1] == self.won[2][0] != ' ':
      return self.won[0][2]
    return 'N'

  def check_legit(self, x, y):
    self.message = '' 
    if self.xcor == -1 and self.ycor == -1:
      pass
    elif not self.board[x][y]== '.':
      self.message = 'Square has already been taken!' 
    elif not self.won[self.xcor][self.ycor] == ' ':
      self.message = 'Square has already been won! (If you were supposed to put in this square, you can put in any square!)' 
    elif not self.check_square(x, y):
      self.message = "Wrong square?"
    return self.message
  
  def move(self, x, y):
    square_x = x%3
    square_y = y%3
    if self.check_legit(x, y) != '':
      return self.message 
    self.board[x][y] = self.turn 
    if not self.check_small_win(x, y) == 'N':
      self.won[self.xcor][self.ycor] = self.check_small_win(x, y)
      print(self.won[self.xcor][self.ycor] + " has won " + str(self.xcor) + ", " + str(self.ycor) + "!")
      # self.xcor = -1 
      # self.ycor = -1 
      if not self.check_big_win() == 'N':
        self.message += self.check_big_win()
        self.message += " has won!"
        self.game_ended = True 
        return self.message
    if self.turn == 'X':
      self.turn = 'O'
    else:
      self.turn = 'X'
    self.message = "Move successful!"
    # self.anywhere should be true if 
    # 1. no space in square
    # 2. square has been won
    square_x = x%3
    square_y = y%3
    self.xcor = square_x 
    self.ycor = square_y
    if self.won[self.xcor][self.ycor] != ' ':
      self.xcor = -1 
      self.ycor = -1 
    return self.message 
    
  def print(self):
  	string = ''
    string += "  "
    for i in range(1, 10):
      string += str(i)
      if i%3 == 0:
        string += " "
    string += '\n' 
    for i in range(0, 9):
      string += str(i+1) + " " 
      for j in range(0, 9):
        string += self.board[i][j]
        if (j+1)%3 == 0:
          string += ' '
      string += '\n' 
      if (i+1)%3 == 0:
        string += '\n' 
    
    # self.message = "Turn has been made!"
    # return self.message 

ttt = tictactoe()
while not ttt.game_ended:
  ttt.print()
  move_x = input("Insert x coordinate: ")
  move_y = input("Insert y coordinate: ")
  if " " in move_x or " " in move_y:
    print("Invalid coordinate!")
    continue 
  if int(move_x) <= 0 or int(move_x) > 9 or int(move_y) <= 0 or int(move_y) > 9:
    print("Invalid coordinate!")
    continue 
  print(ttt.move(int(move_x)-1, int(move_y)-1))
  print("Next move must be in: ", end="")
  print(ttt.xcor+1, end=", ")
  print(ttt.ycor+1)
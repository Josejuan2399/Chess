chess_map_from_alpha_to_index = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}

chess_map_from_index_to_alpha = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}


class Chessboard():
  
  def __init__(self):
    
    self.board = []
    self.occupiedSpaces = []
    
    for columns in range(8):
      for rows in range(1,9):
        self.board.append(chess_map_from_index_to_alpha[columns] + str(rows))
    
  def showBoard(self):
    return self.board

class Piece():
  
  def __init__(self, pos):
        self.column, self.row = list(pos.strip().lower())
        self.row = int(self.row) 
        self.column = chess_map_from_alpha_to_index[self.column]
        self.solutionMoves = []
        self.firstMove = 0
    
  def showPos(self):
    return [chess_map_from_index_to_alpha[self.column] + str(self.row)]

class Pawn(Piece):
  
  def __init__(self, pos):
     Piece.__init__(self,pos)

class Rook(Piece):
  
  def __init__(self, pos):
    Piece.__init__(self, pos)
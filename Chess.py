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
        self.availableSpaces = []

        for columns in range(8):
          for rows in range(1,9):
            self.board.append(chess_map_from_index_to_alpha[columns] + str(rows))
    
    def showBoard(self):
        return self.board

    def occupiedSpace(self, pos):
        self.occupiedSpaces.append(pos)
        self.occupiedSpaces.sort()
        
    def showOccupiedSpace(self):
        return self.occupiedSpaces

    def showAvailableSpaces(self):
        for spaces in self.showBoard():
            if (spaces not in self.occupiedSpaces):
                self.availableSpaces.append(spaces)
        return self.availableSpaces


class Piece():
  
  def __init__(self, pos, board):
        self.column, self.row = list(pos.strip().lower())
        self.row = int(self.row) 
        self.column = chess_map_from_alpha_to_index[self.column]
        self.solutionMoves = []
        self.firstMove = 0
        board.occupiedSpace(chess_map_from_index_to_alpha[self.column] + str(self.row))
    
  def showPos(self):
    return [chess_map_from_index_to_alpha[self.column] + str(self.row)]

class Pawn(Piece):
  
  def __init__(self, pos, board):
     Piece.__init__(self, pos, board)

class Rook(Piece):
  
  def __init__(self, pos, board):
    Piece.__init__(self, pos, board)

class Bishop(Piece):
  
  def __init__(self, pos, board):
    Piece.__init__(self, pos, board)

class Queen(Rook, Bishop):
  
  def __init__(self, pos, board):
    Piece.__init__(self, pos, board)

board1 = Chessboard()
piece1 = Piece("a2", board1)

piece2 = Piece("a5", board1)

piece3 = Piece("a3", board1)


print board1.showOccupiedSpace()
print board1.showAvailableSpaces()


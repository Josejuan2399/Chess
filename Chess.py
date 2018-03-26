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
        if (pos not in board.occupiedSpaces):
            self.column, self.row = list(pos.strip().lower())
            self.row = int(self.row) 
            self.column = chess_map_from_alpha_to_index[self.column]
            self.solutionMoves = []
            self.firstMove = 0
            board.occupiedSpace(chess_map_from_index_to_alpha[self.column] + str(self.row))
        else:
            print ("Occupied Space")
    
  def showPos(self):
    return [chess_map_from_index_to_alpha[self.column] + str(self.row)]

class Pawn(Piece):
  
    def __init__(self, pos, board):
        Piece.__init__(self, pos, board)

    def getPawnMoves(self):
        self.solutionMoves = []
        if (self.firstMove == 0 and self.row == 2):
          
          for steps in range(1,3):
            self.solutionMoves.append(chess_map_from_index_to_alpha[self.column] + str(self.row + steps))
        elif(self.row != 8):
          self.solutionMoves.append(chess_map_from_index_to_alpha[self.column] + str(self.row + 1))
        
        return self.solutionMoves


class Rook(Piece):

    def __init__(self, pos, board):
        Piece.__init__(self, pos, board)

    def getRookMoves(self):
        self.solutionMoves = []

        # Compute the moves in column
        for j in range(8):
          if j != self.column:  
            self.solutionMoves.append(chess_map_from_index_to_alpha[j] + str(self.row))

        # Compute the moves in row
        for i in range(1,9):
            if i != self.row:
              self.solutionMoves.append(chess_map_from_index_to_alpha[self.column] + str(i))
        
        self.solutionMoves.sort()
        return self.solutionMoves

class Bishop(Piece):
  
  def __init__(self, pos, board):
    Piece.__init__(self, pos, board)

class Queen(Rook, Bishop):
  
  def __init__(self, pos, board):
    Piece.__init__(self, pos, board)

board1 = Chessboard()
piece1 = Piece("a3", board1)

rook1 = Rook("a5", board1)

pawn1 = Pawn("a2", board1)
piece1.showPos()


# print board1.showOccupiedSpace()
# print board1.showAvailableSpaces()

print pawn1.getPawnMoves()
print rook1.getRookMoves()




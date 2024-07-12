import random

class TicTacToe:

    def __init__(self):
        """Initialize with empty board"""
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def show(self):
        """Format and print board"""
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def clearBoard(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def whoWon(self):
        if self.checkWin() == "X":
            return "X"
        elif self.checkWin() == "O":
            return "O"
        elif self.gameOver() == True:
            return "Nobody"

    def availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getMoves(self, player):
        """Get all moves made by a given player"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def makeMove(self, position, player):
        """Make a move on the board"""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        elif self.board[position] != " " and player is " " :
            self.board[position] = player
            return True
        else:
            print("Invalid Move")
            return False

    def checkWin(self):
        """Return the player that wins the game"""
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        """Return True if X wins, O wins, or draw, else return False"""
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    
    def minimax(self, board, depth, player):
        if player == "O":
            best = [-1, float('-inf')]
        else:
            best = [-1, float('inf')]
    
        if depth == 0 or self.gameOver():
            if self.checkWin() == "O":
                return [-1, -1]  # Human wins
            elif self.checkWin() == "X":
                return [-1, 1]   # AI wins
            else:
                return [-1, 0]   # Draw
    
        for move in self.availableMoves():
            board.makeMove(move, player)
            score = self.minimax(board, depth - 1, changePlayer(player))
            board.makeMove(move, " ")
            score[0] = move
    
            if player == "O":
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score
    
        return best



def changePlayer(player):
    """Returns the opposite player given any player"""
    if player == "X":
        return "O"
    else:
        return "X"


def make_best_move(board, depth, player):
    if player == "":
      best_move = board.minimax(board, depth, player)[0]
      return best_move
    else:
      raise ValueError("make_best_move function currently only supports 'O' player.")


# Actual game
if __name__ == '__main__':
    game = TicTacToe()
    game.show()

    while game.gameOver() == False:

        isValid = False
        while not isValid:
            person_move = int(input("You are O: Choose number from 1-9: "))
            isValid =  game.makeMove(person_move - 1, "O")
        game.show()

        if game.gameOver() == True:
            break

        print("Computer choosing move...")
        ai_move = make_best_move(game, -1, "X")
        game.makeMove(ai_move, "X")
        game.show()

print("Game Over. " + game.whoWon() + " Wins")

import random
#lets make a class for player
class Player:
    def __init__(self, letter):
        #the letter will be x or o
        self.letter = letter
        # we want all players to get their next move
        def get_move(self, game):
            pass
#inheriting the 'player' class in a randomcomputer class

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
      square = random.choice(game.available_moves())
      return square
#integrating the 'player' class in a humanplayer class
class HumanPlayer(Player):
    def __init__(self, letter):
      super().__init__(letter)

    def get_move(self, game):
      valid_square = False
      val = None
      while not valid_square:
        square = input(self.letter + "\'s turn. Input move (0-8):")
        #we are going to check that this is a correct value by trying to cast
        # it to an integer, if it isnt then we say its invalid
        #if that spot is not available on the board we also say its invalid
        try:
          val = int(square)
          if val not in game.available_moves():
            raise ValueError
          valid_square = True
        except ValueError:
          print("Invalid square, try again")
      return val
#making the game
class TicTacToe:
  def __init__(self):
    self.board = ['' for _ in range(9)]
    #we will use single list to represent 3x3 board
    self.current_winner = None
    #to keep track of winner

  def print_board(self):
    #this is to get the rows
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print('| ' + ' | ' .join(row) + ' |')
  @staticmethod
  def print_board_nums():
    #0 | 1 | 2 etc tells us what number tells us what number corresponds to what box
      number_board = [[str(i) for i in range(j*3,(j+1)*3)]for j in range(3)]
      for row in number_board:
        print('| ' + ' | ' .join(row) + ' |')
  def available_moves(self):
    return [i for i, spot in enumerate(self.board) if spot == '']
    # return []
    # moves = []
    # for (i, x) in enumerate (self.board):
    #     ['x', 'x', 'o'] --> [(0,'x'),(1,'x'),(2,'o')]
    #     if spot == '':
    #         moves.append(i)
    # return moves

  def empty_squares(self):
    return '' in self.board

  def num_empty_squares(self):
    return self.board.count('')

  def make_move(self, square, letter):
    #if the valid move, then make the move, then return true
    #if invalid then return false
    if self.board[square] == '':
      self.board[square] = letter
      if self.winner(square, letter):
        self.current_winner = letter
      return True
    return False
  def winner(self, square, letter):
    #winner is 3 in a row colum or diagonal
    #first we will do row
    row_ind = square//3
    row = self.board[row_ind*3 : (row_ind +1)*3]
    if all([spot == letter for spot in row]):
      return True

    #now we will see the column1
    col_ind = square % 3
    column = [self.board[col_ind+i*3] for i in range (3)]
    if all([spot == letter for spot in column]):
      return True

    # now we check diagonals
    # the diagonal moves can only be on the squares 0, 2, 4, 6 or 8
    if square % 2 == 0:
      diagonal1 = [self.board[i] for i in [0, 4, 8]]
      #left to right diagonal
      if all([spot == letter for spot in diagonal1]):
        return True
      diagonal2 = [self.board[i] for i in [2, 4, 6]]
      #right to left diagonal
      if all ([spot == letter for spot in diagonal2]):
        return True
#playing the game
def play(game, x_player, o_player, print_game=True):
  # return the winner(the letter they used) or 'none' for a tie
  if print_game:
    game.print_board_nums()
  letter = 'X'
  #starting letter
  #iterate while the game still has empty squares
  #(we dont have to worry about the winner bcs we'll just return that  which'll break the loop
  while game.empty_squares():
    #get the move from the appropriate player
    if letter == 'O':
        square = o_player.get_move(game)
    else:
        square = x_player.get_move(game)
  # now we will define a function to make a move
    if game.make_move(square, letter):
      if print_game:
        print(letter + f' made a move to square {square}')
        game.print_board()
        print(' ') #just  empty line

      if game.current_winner:
        if print_game:
          print(letter + 'wins!' )
          break
        #after we made our move, we need to alternate letters
    if letter == 'X':
      letter = 'O'
    else:
      letter = 'X'
    if print_game:
      print('It \'s a tie!')
#actually print the game

def choose_game_mode():
    while True:
      choice = input("Choose game mode:\n1. Player vs Player\n2. Computer vs Player\nEnter your choice (1 or 2): ")
      if choice in ['1', '2']:
        return int(choice)
      else:
        print("Invalid choice. Please enter 1 or 2.")


def play_again():
  while True:
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    if choice in ['yes', 'no']:
      return choice == 'yes'
    else:
      print("Invalid choice. Please enter 'yes' or 'no'.")


def main():
  while True:
    game_mode = choose_game_mode()

    x_player = HumanPlayer('X')
    if game_mode == 1:
      o_player = HumanPlayer('O')
    else:
      o_player = RandomComputerPlayer('O')

    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

    if not play_again():
      break


if __name__ == '__main__':
  main()
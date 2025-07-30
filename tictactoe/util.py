from enum import Enum

class SYMBOL(Enum):
    X = 'X'
    O = 'O'


class Player:

    def __init__(self,name,symbol:SYMBOL):
        self.name = name
        self.symbol = symbol


class Board:

    def __init__(self,size):
        self.__board = [[None for _ in range(size)] for _ in range(size)]
        self.__size = size
        self.__moves_made = 0

    def get_board(self):
        return self.__board
    
    def get_size(self):
        return self.__size
    
    def print_board(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board[0])):
                if self.__board[i][j] is None:
                    print('_', end=' ')
                else:
                    print(self.__board[i][j], end=' ')
            print()

    def check_row(self,row,symbol):

        for j in range(len(self.__board[0])):
            if self.__board[row][j] != symbol:
                return False
            
        return True
    
    def check_col(self,col,symbol):

        for i in range(len(self.__board)):
            if self.__board[i][col] != symbol:
                return False
        return True
    
    def check_diag_first(self,symbol):

        # first diag
        for i in range(self.__size):
            if self.__board[i][i] != symbol:
                return False
            
        return True

    def check_diag_secon(self,symbol):

        for i in range(self.__size-1 ,-1,-1):
            if self.__board[i][self.__size - i -1] != symbol:
                return False
            
        return True
    
    def can_move(self):

        return self.__moves_made < (self.__size*self.__size)


    def make_move(self,player: Player,i:int,j:int):

        if i<0 or i>= self.__size or j<0 or j>=self.__size:
            print('Invalid oprtion')
            return False

        if self.__board[i][j] is not None:
            print('Invalid move')
            return False
        
        self.__board[i][j] = player.symbol.value
        self.__moves_made+=1

    def clear_board(self):
        self.__board = [[None for _ in range(self.__size)] for _ in range(self.__size)]
        print('Board cleared')

    
class Game:

    def __init__(self, board: Board, players: list[Player]):
        self.__board = board
        self.__players = players
        self.__current_player = 0
        self.__winner = None
        self.__draw = False


    def set_first_player(self, player: Player):

        if player not in self.__players:
            print('Invalid player')
            return False
        self.__current_player = player

    
    def print_board(self):
        self.__board.print_board()

    def check_winner(self):

        #rows
        for player in self.__players:
            for i in range(self.__board.get_size()):
                if self.__board.check_row(i,player.symbol.value):
                    self.__winner = player

                if self.__board.check_col(i,player.symbol.value):
                    self.__winner = player

                if self.__board.check_diag_first(player.symbol.value):
                    self.__winner = player

                if self.__board.check_diag_secon(player.symbol.value):
                    self.__winner = player

        if self.__winner is not None:
            print(f'we have a winner ${self.__winner.name}')

        return self.__winner is not None


    def play(self):

        currP = 0
        while True:
            if self.__board.can_move():
                self.__current_player = self.__players[currP]
                print(f'Current player {self.__current_player.name} {self.__current_player.symbol.value}')
                self.print_board()
                i,j = map(int, input('Enter row and column: ').split())
                self.__board.make_move(self.__current_player, i, j)
                if self.check_winner():
                    print(' match over')
                    break
                currP+=1
                currP%=len(self.__players)
            else:
                self.__draw = True
                break

    

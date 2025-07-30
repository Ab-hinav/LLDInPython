from util import Player,Game,Board,SYMBOL



class TicTacToeDemo:


    @classmethod
    def run(cls):
        player1 = Player('abhi',SYMBOL.X)
        player2 = Player('riya',SYMBOL.O)

        board = Board(3)

        game = Game(board,[player1,player2])

        game.play()





if __name__ == '__main__':
    TicTacToeDemo.run()
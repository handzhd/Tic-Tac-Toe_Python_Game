from player import HumanPlayer, ComputerPlayer, AIComputer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #define board for TicTacToe 3x3
        self.the_winner = None

    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| '+ ' | '.join(row) + ' |') # build the board, ex | | | |
                                                #                     | | | |
                                                #                     | | | |
    @staticmethod  
    def board_nums():
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print('| '+ ' | '.join(row) + ' |')
        # make the board with corresponding num of box 
        # |0|1|2|
        # |3|4|5|
        # |6|7|8|

    def valid_moves(self):
        # get the valid moves, IF the box already has either X or O, then it is invalid moves.
        moves = []
        for i,val in enumerate(self.board): # ex: {0: ' ' , 1: 'X' , 2: 'O'}
            if val == ' ': # it is empty box
                moves.append(i)
        return moves
        # _ _ X
        # O O _
        # X _ _
    
    def empty_box(self):
        dummy = 0
        for row in self.board:
            if row == ' ':
                dummy += 1    
        return dummy
    
    def get_nums_empty_box(self):
        return self.board.count(' ')
    
    def make_move(self, box, char):
        if self.board[box] == ' ':
            self.board[box] = char
            if self.winner(box, char):
                self.the_winner = char
            return True
        return False

    def winner(self, box, char):
        # 3 ways to win the game: by successfully fill the same char in row, col, or diagonally. 

        # for row's way
        row_ind = box // 3   # round-down the answer
        row = self.board[row_ind*3 : (row_ind+1)*3]    
        if all([spot == char for spot in row]):
            return True
            
        # for column's way
        col_ind = box % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == char for spot in col]):
            return True
        
        # diagonal's way
        if box % 2 == 0:
            diag1 = [self.board[i] for i in [0,4,8]]
            if all([spot == char for spot in diag1]):
                return True
            diag2 = [self.board[i] for i in [2,4,6]]
            if all([spot == char for spot in diag2]):
                return True
        
        return False
            

def play(game, x_player, o_player, select_mode, print_game = True):

    if print_game:
        game.board_nums()
    
    char = 'X' # 1st player
    
        
    while game.empty_box():
        if char == 'O': # executed function for corresponding player
            box = o_player.get_move(game)
        else:
            box = x_player.get_move(game)

        
        if game.make_move(box, char):
            if print_game:
                print(char + f' moves to box {box}')
                game.print_board()
                print('')

            if game.the_winner:
                if print_game:
                    print(char + ' player is the winner! \n')
                    return char

            #switch player    
            if char == 'X':
                char = 'O'
            else:
                char = 'X'

            time.sleep(0.5)

    # while stop the looping
    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    print('1: Human vs Human \n2: Human vs Computer \n3: Computer vs Computer')
    select_mode = int(input('Select mode to play TicTacToe: '))

    while True:    
        if select_mode == 1:
            x_player = HumanPlayer('X')
            o_player = HumanPlayer('O')
            break
        elif select_mode == 2:
            x_player = HumanPlayer('X')
            o_player = AIComputer('O')
            break
        elif select_mode == 3:
            x_player = AIComputer('X')
            o_player = ComputerPlayer('O')
            break
        else:
            print('Invalid input. Please try again')
            select_mode = int(input('Select mode to play TicTacToe: '))
            
    print('The game is starting!')
    start = TicTacToe()
    play(start, x_player, o_player, select_mode, print_game=True)

            
        




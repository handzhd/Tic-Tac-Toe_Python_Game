import math, random

class Player:
    def __init__(self, char):
        self.char = char

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, char):
        super().__init__(char)

    def get_move(self, game):
        valid_box = False
        val = None

        while not valid_box:
            box = input(self.char + '\'s turn. Input from 0-8: ')
            
            try:
                val = int(box)
                if val not in game.valid_moves():
                    raise ValueError
                valid_box = True
            except ValueError:
                print('Invalid input. Please try again!')
            
        return val

class ComputerPlayer(Player):
    def __init__(self, char):
        super().__init__(char)

    def get_move(self, game):
        box = random.choice(game.valid_moves())
        return box

class AIComputer(Player):
    def __init__(self, char):
        super().__init__(char)

    def get_move(self, game):

        # base case, if the computer starts first, just put on random box
        if len(game.valid_moves()) == 9:
            box = random.choice(game.valid_moves())
        else: # if there is at least one box filled in, use the algorithm to determine the winner
            box = self.minmax(game, self.char)['position']
            
        return box
        
    def minmax(self, con, player):
        max_player = self.char # this one is human
        other_player = 'O' if player == 'X' else 'X'

        # first, check if the previous move is the winner
        # BASE case
        if con.the_winner == other_player:
            return {
                'position' : None,
                'value' : 1 * (con.get_nums_empty_box() + 1) if other_player == max_player else
                -1 * (con.get_nums_empty_box() + 1)
            }
        elif not con.empty_box(): # if all the box is filled out and no one is the winner / TIE
            return {
                'position' : None,
                'value' : 0
            }
        
        if player == max_player:
            player_cond = {
                'position' : None,
                'value' : -math.inf # with this variable, we can always get the bigger number when we update it 
            }
        
        else:
            player_cond = {
                'position' : None,
                'value' : math.inf # we can also always get the smaller number when we update it
            }

        for valid_box in con.valid_moves():
            # 1st step, try to fill in the box
            con.make_move(valid_box, player)

            # 2nd recursively do for the other player would move based on the algorithm of min and max
            recursive_move = self.minmax(con, other_player)

            # 3rd restore all the move after the recursive
            con.board[valid_box] = ' ' # restore to empty box
            con.the_winner = None      # the winner is updated after recursive program, we want to return it to before the recursive
            recursive_move['position'] = valid_box

            # 4th update the dictionaries
            if player == max_player:
                if recursive_move['value'] > player_cond['value']:
                    player_cond = recursive_move # get the maximized score
            
            else:
                if recursive_move['value'] < player_cond['value']:
                    player_cond = recursive_move # get the minimized score
        return player_cond

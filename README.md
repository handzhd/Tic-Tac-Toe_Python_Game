# Tic-Tac-Toe_Python_Game
## Description
This is a small project that I did to deepen my knowledge and have a practice learning in python language. The game is consists 3 modes: player v player, player v comp, comp v comp. In this project, there are two type of comp players: randomize and recursive algorithm, which never leads the player win againts it.

## Tools
* Python 3.10.10
* Visual Studio Code

## Modules
Built in modules that I used for this project.

```
import math
import random
import time
```

### Recursive Algorithm

```def minmax(self, con, player)``` is the function inside of the  ```class AIComputer(Player)```  that have an algorithm to calculate all of the possible moves that can happen. Minmax function calculates the possibilities of any moves and return it the value. The algorithm will choose the maximum value while also calculate the minimum value to  The function has an ouput type of dict which consists of position of the last filled in box and the value. 

```
def get_move(self, game):

        # base case, if the computer starts first, just put on random box
        if len(game.valid_moves()) == 9:
            box = random.choice(game.valid_moves())
        else: # if there is at least one box filled in, use the algorithm to determine the winner
            box = self.minmax(game, self.char)['position']
        
        return box
```

This function determine which box that the computer will choose. If the AI computer starts first, it just choose random box in the TicTacToe board. If the AI Computer starts later, then it calculate the possibility and choose the box based on the calculation.

```
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
```
This is one of the base cases in this project. First we want to check if the previous move is the winner. If the condition meets, then we calculate the value. For 'X' player want to get the maximum value as possible which means that it is the optimal move. For 'O' want to get the lowest value as possible with the exact same meaning. IF all the box is filled out, and no one is winner therefore the value will be 0.

```
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
```

This for loop function, simulate all the possibility and find the optimal moves recursively. And ```return player_cond``` is the output for minmax function. 

## References
* I used [this](https://www.freecodecamp.org/news/python-projects-for-beginners/#hangman-python-project) as a guide for this project.
* [Youtube](https://www.youtube.com/watch?v=8ext9G7xspg&t=4553s) for the guidance to this project


###### Note
None of this code is developed by myself. I used references to study and learn about Python

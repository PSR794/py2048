# py2048
## THE 2048 GAME
* The code contains the programs for the game '2048'.
* Python is the programming language used.
### GAME RULES
* It starts with a grid having, a '2' anywhere on the grid.
* PLayer's aim is to generate the target number in the grid to win the game.
* Player will lose if he/she runs out of move, with the target number still not produced.
  #### THE GAME PLAY AND WIN/LOSE SITuATION
  * PLayer has to swipe the grid in the 4 directions according to the choice.
  * After each move a new '2' is spawned in the grud on emoty spaces.
  * swiping leads to the numberes shift to the last available empty space in the direction the grid is swiped.
  * PLayer has to produce a higher by fusing two similar numbers i.e only numbers whose Nth root is '2' can be produced.
  * If the player manages to prduce the target number before there is  no move left i.e, if all spaces are occupied given no two similar numbers are adjacent in both the directions, then the player wins!.
  * another important rule is that, if a number is produced by fusion  o ftwo numbers then that fused number is not fused again with itself in that same move.
  
### ABOUT THE CODE
1. It asks the user to input the grid size and winning number.(input 0 for default settings [5X5 grid with 2048 as winning number])
1. The game starts and the user has to input 'w','a','s' or 'd' for swiping the grid in up,left,down and right directions resp.
1. Every time the user makes a move the code access the elements of grid in that direction to swipe the element step by step, and the grid gets modified.
1. It checks the lose or win conditions at each move and if the numbers cannot be swiped then it asks to try some other move.
1. Other moves like 'e' and 'r'are provided to exit and restart the game at any point.
1. 'c' displays the controls anytime the user wants to.
1. The code displays if the player has lost or won and breaks out of the loop.

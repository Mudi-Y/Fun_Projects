#Tipover

A backtracking script for solving the Tipover game https://www.thinkfun.com/products/tipover/

tipover.dat contains example of a starting configuration for game. 
The rows of tipover.dat contain:
fist row: row x column size of the tipover game board
second row: (row, column) coordinate for the start position
third and beyond: game board with initial values. "." represents an empty square, intiger values represent heights of crate stacks at that location, and "\*" represents the goal. 

If the goal can be reached from the initial state, the game board at the end of the game will be displayed, and the sequence of instructions in the form of the coordinate and crate stack tipping directions will be printed. If the goal can not be reached, the program will output "no solution".
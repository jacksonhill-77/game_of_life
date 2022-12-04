TASK DESCRIPTION

Conway's game of life on an infinite grid, optimised for sparse finite life

In Conway's game of life, there's a square grid, where every cell has eight neighbours (sides, up and down, and diagonals). 

Every cell is either alive or dead. We're going to assume almost all cells are dead, and at the beginning of the game the user will provide a list of all the cell coordinates that are alive.

On each step of the game,
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell. (reproduction)
3. All other live cells die in the next generation (under- or over-population), and all other dead cells stay dead.

As well as the list of live cells, the user will specify the number of steps the game should run for. At the end, the game will print the list of live cells.

Extension (if you want it) is to let the user specify a rectangular section of the grid and (using ascii art or otherwise) show the state of the game within that rectangle on each step of the game (kind of like an animation). (Note: any life that ends up outside the rectangle should still be listed at the end of the game.)

Possible test cases: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns

ASSUMPTIONS

- The grid cells can comprise negative numbers
- 

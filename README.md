TASK DESCRIPTION (CONCISE)

Recreate Conway's game of life on an infinite grid while optimising it for sparse finite life (see bottom of page for full description).


REQUIREMENTS

- Python 3 
- pytest 


TO START

1. Navigate to project folder in terminal 
2. With python 3 installed, enter "python main.py" in your command line interface to run the main file
3. Interaction with the script is done through the command line interface. Enter the input parameters manually, or simply press enter to use the default


TO TEST 

1. Navigate to project folder in terminal
2. With pytest installed, enter "pytest ." to run all 3 test files in the folder


ASSUMPTIONS

- The input will be the correct data form (e.g. list of tuples for starting live cells)
- No initial cells will share coordinates
- The grid cells can comprise negative numbers
- The output should be a list of tuples
- There will always be at least one initial alive cell input


DESIGN CHOICES

1. The Cell class could have been implemented as a tuple. However, it is implemented as a class to enable future behaviour to be attached to it. e.g. if we wanted to give it a random chance of survival or create sub-classes of cells, this is easier if it is a class.

2. One option could have been to generate an entire grid, populating it with the original alive cells, and then looping over the whole grid to find the alive cells for each step, where the time complexity is O(A*B) for the x * y dimensions of the grid.

However, the approach I used optimised the game for sparse finite life by only searching for the cells which could become live on the next step. These are the current live cells and all 8 adjacent cells for each original live cell. The time complexity here would simply be O(A).

3. The getAdjacentCells function is put in the Cell class, keeping the GamePlayer class cleaner but also putting it in a place that thematically makes sense.


TASK DESCRIPTION (FULL)

In Conway's game of life, there's a square grid, where every cell has eight neighbours (sides, up and down, and diagonals). 

Every cell is either alive or dead. We're going to assume almost all cells are dead, and at the beginning of the game the user will provide a list of all the cell coordinates that are alive.

On each step of the game,
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell. (reproduction)
3. All other live cells die in the next generation (under- or over-population), and all other dead cells stay dead.

As well as the list of live cells, the user will specify the number of steps the game should run for. At the end, the game will print the list of live cells.

Extension (if you want it) is to let the user specify a rectangular section of the grid and (using ascii art or otherwise) show the state of the game within that rectangle on each step of the game (kind of like an animation). (Note: any life that ends up outside the rectangle should still be listed at the end of the game.)

Possible test cases: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns

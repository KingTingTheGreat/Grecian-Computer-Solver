# Greek Computer Solver
Solves the [Project Genius Grecian Computer Puzzle](https://projectgeniusinc.com/grecian-computer/)

## The files
I've created two classes, one for the rings of the puzzle and one for the puzzle itself. The main file is the entry point and will solve then print the puzzle in it's solved state.

## How to read the output
Each "]" represents a level where one "]_x_" means that _x_ is on the base ring, "]]_x_" means that _x_ is on the ring above the base ring, and so on.

## How it works
To find a solution, we simply brute force through the 20,736 (12^4) permutations until we find a solution.

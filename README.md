# sudoku

Sudoku generator (and solver). The solver relies on backtrack.

## generator

To generate a random game:

```
$ ./game.py
sudoku:
. . .  5 . 4  . 7 9
6 . .  . . 8  . . .
. . .  9 . 6  . . .

7 4 6  3 . 9  . 5 .
. . .  . 1 .  . 6 .
3 . 5  . . .  . . 8

. . .  . . .  . 3 .
1 3 7  . . .  . 8 .
8 6 .  . 5 .  9 2 1
solution? [Y/n] 
```

## solver

To solve that hard Sudoku you're struggling with:

```python
>>> from sudoku import Sudoku
>>> g = [[0, 0, 5, 3, 0, 0, 0, 0, 0],
...      [8, 4, 9, 0, 0, 7, 0, 0, 0], 
...      [7, 0, 0, 0, 5, 9, 0, 0, 0],
...      [0, 3, 0, 0, 0, 0, 0, 8, 2],
...      [4, 0, 0, 0, 0, 0, 5, 0, 0],
...      [1, 0, 0, 0, 0, 8, 0, 3, 0],
...      [0, 8, 0, 4, 0, 0, 2, 0, 6],
...      [0, 0, 0, 0, 0, 0, 0, 0, 0],
...      [6, 0, 0, 5, 0, 3, 4, 0, 0]]
>>> s = Sudoku(g)
>>> s.solve()
>>> print(s)
2 1 5  3 8 4  6 9 7
8 4 9  6 1 7  3 2 5
7 6 3  2 5 9  8 4 1

9 3 6  7 4 5  1 8 2
4 7 8  1 3 2  5 6 9
1 5 2  9 6 8  7 3 4

3 8 7  4 9 1  2 5 6
5 2 4  8 7 6  9 1 3
6 9 1  5 2 3  4 7 8
```

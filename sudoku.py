#!/usr/bin/env python3
# @author: l3nn4rt

from random import shuffle
from copy import deepcopy

class Sudoku:
    def __init__(self, grid=None, hints=0):
        '''Sudoku reflecting a given grid, if any, or randomly initialized.'''
        self.pairs = [(i, j) for i in range(9) for j in range(9)]
        if grid:
            self.grid, sols = deepcopy(grid), []
            self.solve(sols, 2)
            if len(sols) > 1:
                raise Exception('multiple solutions found')
        else:
            self.random_init(hints)

    def __str__(self):
        s = ''
        for i in range(9):
            if i and not i % 3:
                s += '\n'
            for j in range(9):
                if j and not j % 3:
                    s+= ' '
                s += str(self.grid[i][j] or '.') + (' ' if j < 8 else '')
            if i != 8:
                s += '\n'
        return s

    def row(self, i):
        return self.grid[i]

    def col(self, j):
        return [self.grid[i][j] for i in range(9)]

    def block(self, i, j):
        '''Block containing cell `(i, j)` flattened.'''
        return [n for r in self.grid[i-i%3:i-i%3+3] for n in r[j-j%3:j-j%3+3]]

    def options(self, i, j):
        '''Candidates for cell `(i, j)`.'''
        used = set(self.row(i) + self.col(j) + self.block(i, j))
        return [n for n in range(1, 10) if n not in used]

    def empty(self):
        '''Generator of empty cells coordinates.'''
        for i, j in self.pairs:
            if not self.grid[i][j]:
                yield i, j

    def filled(self):
        '''List of filled cells coordinates.'''
        return [p for p in self.pairs if not p in self.empty()]

    def solve(self, sols=[], maxsol=1, randomize=False):
        '''Solve Sudoku with the backtrack technique.'''
        pair = next(self.empty(), None)
        if not pair:
            # solution found
            sols.append(deepcopy(self.grid))
            return
        i, j = pair
        opts = self.options(i, j)
        if not opts:
            # no number can be placed here: backtrack
            return
        if randomize:
            shuffle(opts)
        for opt in opts:
            # put a number here
            self.grid[i][j] = opt
            self.solve(sols, maxsol, randomize)
            if len(sols) == maxsol:
                # maxsol solutions found: terminate recursion
                return
            self.grid[i][j] = 0

    def random_init(self, hints=0):
        '''Initialize Sudoku with `hints` cells filled.'''
        # fill grid with a random solution
        self.grid, sols = [9 * [0] for i in range(9)], []
        self.solve(sols, 1, True)
        self.grid = sols[0]
        # take unnecessary numbers out of the grid
        pairs = self.filled()
        shuffle(pairs)
        for i, j in pairs:
            n, self.grid[i][j] = self.grid[i][j], 0
            backup, sols = deepcopy(self.grid), []
            self.solve(sols, 2)
            self.grid = backup
            if len(sols) > 1:
                self.grid[i][j] = n
            if len(self.filled()) == hints > 0:
                break

    def check(self):
        '''Raise an Exception if any game constraint is violated.'''
        for idx in range(9):
            for n in range(1, 10):
                if self.row(idx).count(n) > 1:
                    raise Exception(f'row {idx}: multiple {n} found')
                if self.col(idx).count(n) > 1:
                    raise Exception(f'col {idx}: multiple {n} found')
                if self.block(*[3 * c for c in divmod(idx, 3)]).count(n) > 1:
                    raise Exception(f'blk {idx}: multiple {n} found')

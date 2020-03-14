#!/usr/bin/env python3
# @author: l3nn4rt

from sudoku import Sudoku

def main():
    s = Sudoku(hints=30)
    s.check()
    print(f'sudoku:')
    print(s)

    if 'yes'.startswith(input('solution? [Y/n] ').lower()):
        s.solve()
        print(f'solution:')
        print(s)

if __name__ == '__main__':
    main()

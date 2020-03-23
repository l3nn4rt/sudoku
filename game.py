#!/usr/bin/env python3
# @author: l3nn4rt

from sudoku import Sudoku

def main():
    s = Sudoku(hints=30)
    s.check()
    print('sudoku:')
    print(s)

    if 'yes'.startswith(input('solution? [Y/n] ').lower()):
        s.solve()
        print('solution:')
        print(s)

if __name__ == '__main__':
    main()

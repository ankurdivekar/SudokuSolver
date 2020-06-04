import sys
import numpy as np


class SudokuSolver():

    def __init__(self):
        self.grid = None
        sys.setrecursionlimit(10 ** 6)

    def get_grid_from_image(self, img_path):
        raise NotImplementedError

    def solve_grid(self, grid):
        self.grid = grid
        print('\nSolving...\n')
        self.solve()
        print(np.array(self.grid))

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for number in range(1, 10):
                        if self.can_insert(y, x, number):
                            self.grid[y][x] = number
                            print(f'{number} inserted at ({y},{x})')
                            # print(np.array(self.grid))
                            # input('Proceed?')
                            self.solve()

                            print(f'Backtracking for ({y},{x}) with {number}')
                            self.grid[y][x] == 0
                            # print(np.array(self.grid))
                    return
        # print(np.array(self.grid))

    def can_insert(self, row, col, n):
        # Check row for number
        for i in range(9):
            if self.grid[row][i] == n:
                return False

        # Check column for number
        for i in range(9):
            if self.grid[i][col] == n:
                return False

        # Get indexes of 9-box containing (row,col)
        x = (col // 3) * 3
        y = (row // 3) * 3
        # Check 9-box for number
        for i in range(y, y + 3):
            for j in range(x, x + 3):
                if self.grid[i][j] == n:
                    return False

        # If number not found anywhere
        return True

    # def get_sudoku_str(self, grid):
    #     s = '\n'.join(''.join(str(row) for row in col) for col in grid)
    #     s = s.replace(' ', '.').replace('0', '-').replace('_', '.')
    #     print(s)


if __name__ == "__main__":

    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print(np.array(grid))
    sudoku = SudokuSolver()
    sudoku.solve_grid(grid)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

sudoku_grid = []

for row in range(9):
    sudoku_grid.append(list(map(int, input().split())))

row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
subgrid_used = [[False] * 10 for _ in range(9)]

for row in range(9):
    for col in range(9):
        if sudoku_grid[row][col] != 0:
            number = sudoku_grid[row][col]
            row_used[row][number] = True
            col_used[col][number] = True
            subgrid_index = 3 * (row // 3) + (col // 3)
            subgrid_used[subgrid_index][number] = True

def solve_sudoku(cell_index):
    if cell_index == 81:
        for row in sudoku_grid:
            print(" ".join(map(str, row)))
        sys.exit()

    row = cell_index // 9
    col = cell_index % 9

    if sudoku_grid[row][col] != 0:
        solve_sudoku(cell_index + 1)
    else:
        for num in range(1, 10):
            subgrid_index = 3 * (row // 3) + (col // 3)
            if not row_used[row][num] and not col_used[col][num] and not subgrid_used[subgrid_index][num]:
                row_used[row][num] = col_used[col][num] = subgrid_used[subgrid_index][num] = True
                sudoku_grid[row][col] = num
                solve_sudoku(cell_index + 1)
                sudoku_grid[row][col] = 0
                row_used[row][num] = col_used[col][num] = subgrid_used[subgrid_index][num] = False

solve_sudoku(0)

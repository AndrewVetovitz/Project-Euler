def findAllPaths(grid):
    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

def main():
    size = 21
    grid = [[1] * size] * size

    findAllPaths(grid)

    print(grid[20][20])

main()

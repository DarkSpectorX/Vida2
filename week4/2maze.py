def isSafe(grid, x, y, n, smat):

    return 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and smat[x][y] == 0

def rat(grid, x, y, n, smat):
    #Base case or reach the destination
    if x == n - 1 and y == n - 1:
        smat[x][y] = 1
        return True

    # Check current home for movement
    if isSafe(grid, x, y, n, smat):
        smat[x][y] = 1  # Mark home as visited

        # Down
        if rat(grid, x + 1, y, n, smat):
            return True
        # Right
        if rat(grid, x, y + 1, n, smat):
            return True
        # Up
        if rat(grid, x - 1, y, n, smat):
            return True
        # Left
        if rat(grid, x, y - 1, n, smat):
            return True

        smat[x][y] = 0  # Return from the wrong path
        return False
    return False

# Input (hardcoded)
grid = [
    [1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

n = len(grid)

# Answer matrix (path)
smat = [[0 for _ in range(n)] for _ in range(n)]

# Run fanc
rat(grid, 0, 0, n, smat)

# Print result
for i in range(n):
    for j in range(n):
        print(smat[i][j], end=" ")
    print()

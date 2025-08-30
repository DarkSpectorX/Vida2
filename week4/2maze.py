def isSafe(grid, x, y, n):
    return 0 <= x < n and 0 <= y < n and grid[x][y] == 1

def rat(grid, x, y, n, smat):
    if x == n - 1 and y == n - 1:
        smat[x][y] = 1
        return True

    if isSafe(grid, x, y, n):
        smat[x][y] = 1

        if rat(grid, x + 1, y, n, smat):
            return True
        if rat(grid, x, y + 1, n, smat):
            return True

        smat[x][y] = 0  # Backtrack
        return False
    return False

# Input
grid =  [
        [1,0,0,0],
        [1,0,0,1],
        [1,1,0,0],
        [1,1,1,1],
        ]
n= 4

smat = [[0 for _ in range(n)] for _ in range(n)]

rat(grid, 0, 0, n, smat)

# Output
for i in range(n):
    for j in range(n):
        print(smat[i][j], end=" ")
    print()

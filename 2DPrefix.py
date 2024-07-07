def get2DPrefix(self, grid):
    m, n = len(grid), len(grid[0])
    prefix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] + grid[i][j] - prefix[i][j]
    return prefix
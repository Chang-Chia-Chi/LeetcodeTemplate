dp = [[float('inf')] * n for _ in range(n)]

for u, v, t in graph:
    dp[u][v] = t
    dp[v][u] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n, m, mod = len(grid), len(grid[0]), 10**9 + 7
        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 1
        for i in range(n):
            for j in range(m):
                cell = dp[i][j]
                if j > 0:
                    left = dp[i][j - 1]
                    cell[0] += left[0] + left[1] if grid[i][j - 1] == 0 else left[1]
                if i > 0:
                    up = dp[i - 1][j]
                    cell[1] += up[0] + up[1] if grid[i - 1][j] == 0 else up[0]
                cell[0] %= mod
                cell[1] %= mod
        return (dp[n - 1][m - 1][0] + dp[n - 1][m - 1][1]) % mod
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rowCount = m*[0]
        colCount = n*[0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1

        result = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1) and (rowCount[i] > 1 or colCount[j] > 1):
                    result += 1

        return result
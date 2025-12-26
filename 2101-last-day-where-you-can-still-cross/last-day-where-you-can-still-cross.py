from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        days = [[0]*col for _ in range(row)]
        for d, (r, c) in enumerate(cells, start=1):
            days[r-1][c-1] = d

        def can(day):
            queue = deque()
            visited = [[False]*col for _ in range(row)]
            for j in range(col):
                if days[0][j] > day:
                    queue.append((0, j))
                    visited[0][j] = True
            while queue:
                i, j = queue.popleft()
                if i == row-1:
                    return True
                for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < row and 0 <= nj < col and not visited[ni][nj] and days[ni][nj] > day:
                        visited[ni][nj] = True
                        queue.append((ni, nj))
            return False

        low, high = 0, row*col
        while low < high:
            mid = (low+high+1)//2
            if can(mid):
                low = mid
            else:
                high = mid-1
        return low
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}

        for i, row in enumerate(classroom):
            for j, val in enumerate(row):
                if val == "S": sx, sy = i, j
                elif val == "L": litter[(i, j)] = 1 << len(litter)
        full = (1 << len(litter)) - 1
        best = {(sx, sy, 0): energy}
        q = collections.deque([(sx, sy, 0, energy, 0)])

        while q:
            x, y, mask, e, steps = q.popleft()
            if mask == full: return steps
            if e == 0: continue

            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != "X":
                    ne = energy if classroom[nx][ny] == "R" else e - 1
                    nmask = mask | litter.get((nx, ny), 0)

                    if ne > best.get((nx, ny, nmask), -1):
                        best[(nx, ny, nmask)] = ne
                        q.append((nx, ny, nmask, ne, steps + 1))
        return -1            
        
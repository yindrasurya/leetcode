class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range (n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        def BFS(node):
            visited[node] = True
            queue = deque([node])
            node, edge = 0, 0
            while queue:
                curr = queue.popleft()
                node += 1
                edge += len(adj[curr])

                for nei in adj[curr]:
                    if visited[nei]:
                        continue
                    visited[nei] = True
                    queue.append(nei)
            edge //= 2
            return edge == (node) * (node - 1) // 2
        res = 0
        for i in range(n):
            if not visited[i]:
                res += BFS(i)
        return res
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in connections:
            px, py = find(u), find(v)
            if px != py:
                parent[px] = py
        
        grid_map = {}
        for i in range(1, c + 1):
            root = find(i)
            if root not in grid_map:
                grid_map[root] = []
            grid_map[root].append(i)
        
        for stations in grid_map.values():
            stations.sort()
        
        online = [True] * (c + 1)
        grid_min_idx = {root: 0 for root in grid_map}
        result = []
        
        for qtype, x in queries:
            if qtype == 1:
                if online[x]:
                    result.append(x)
                else:
                    root = find(x)
                    stations = grid_map[root]
                    idx = grid_min_idx[root]
                    while idx < len(stations) and not online[stations[idx]]:
                        idx += 1
                    if idx < len(stations):
                        grid_min_idx[root] = idx
                        result.append(stations[idx])
                    else:
                        result.append(-1)
            else:
                online[x] = False
        
        return result

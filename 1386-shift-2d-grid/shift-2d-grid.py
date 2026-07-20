class Solution:
    def shiftGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        (q:=deque(chain(*g))).rotate(k)
        return [*batched(q,len(g[0]))]
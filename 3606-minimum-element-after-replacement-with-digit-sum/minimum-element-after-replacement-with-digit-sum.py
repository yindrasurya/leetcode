class Solution:
    def minElement(self, a: List[int]) -> int:
        return min(sum(map(int,str(v))) for v in a)  
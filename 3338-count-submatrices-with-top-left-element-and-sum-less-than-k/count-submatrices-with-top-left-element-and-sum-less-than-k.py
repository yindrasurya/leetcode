class Solution:
    def countSubmatrices(self, g: List[List[int]], k: int) -> int:
        return sum(v<=k for c in zip(*map(accumulate,g)) for v in accumulate(c))
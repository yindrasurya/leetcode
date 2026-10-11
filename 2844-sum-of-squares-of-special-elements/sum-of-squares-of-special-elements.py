class Solution:
    def sumOfSquares(self, a: List[int]) -> int:
        return sum(v*v for i,v in enumerate(a,1) if len(a)%i==0)
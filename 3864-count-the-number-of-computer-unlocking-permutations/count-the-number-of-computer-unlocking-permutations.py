class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        f=1
        for i in range(1,n):
            if complexity[i]<=complexity[0]:
                return 0

        for i in range(1,n): 
            f=(f*i)%(10**9 + 7)
        return f

        


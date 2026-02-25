class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        M = pow(10,9)+7
        @cache
        def dp(seen,i):
            if i >= len(mat): return seen==1
            res=0
            for n in mat[i]:
                res=(res +dp(gcd(n,seen),i+1))%M
            return res
        return dp(prod(range(1,151)),0) % M
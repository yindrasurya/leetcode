class Solution:
    def numTrees(self, n: int) -> int:

        # Approach 1
        @lru_cache(None)
        def dfs(l, r):
            if l == r:
                return 1
            res = 0
            for i in range(l, r):
                res += dfs(l, i) * dfs(i + 1, r)
            return res

        return dfs(0, n)    
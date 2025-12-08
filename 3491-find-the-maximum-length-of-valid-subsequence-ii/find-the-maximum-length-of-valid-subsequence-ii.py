class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]

        for val in nums:
            x = val % k # x = val mod k
            for y in range(k):
                # continue a sequence of x y with x
                dp[y][x] = dp[x][y] + 1
        
        return max(max(dp[i]) for i in range(k))
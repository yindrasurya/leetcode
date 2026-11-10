class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0]
        for i in range(1, n+1):
            if i == 1:
                dp.append(costs[0] + 1)
            elif i == 2:
                dp.append(costs[1] + min(dp[-1] + 1, dp[-2] + 4))
            else:
                dp.append(costs[i - 1] + min(dp[-1] + 1, dp[-2] + 4, dp[-3] + 9))
        return dp[-1]

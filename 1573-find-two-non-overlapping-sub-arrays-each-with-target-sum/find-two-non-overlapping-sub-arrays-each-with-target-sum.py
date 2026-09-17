class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1
        dp = [INF] * n
        ans = INF
        total = 0
        l = 0

        for r in range(n):
            total += arr[r]
            while total > target:
                total -= arr[l]
                l += 1
            if total == target:
                length = r - l + 1
                if l > 0 and dp[l - 1] != INF:
                    ans = min(ans, dp[l - 1] + length)
                dp[r] = length
            if r > 0 and dp[r - 1] != INF:
                dp[r] = min(dp[r], dp[r - 1])

        return ans if ans != INF else -1
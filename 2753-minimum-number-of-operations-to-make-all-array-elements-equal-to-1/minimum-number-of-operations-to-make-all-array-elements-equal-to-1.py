class Solution:
    def gcd(self, a, b):
        if b == 0:
            return abs(a)
        else:
            return self.gcd(b, a % b)

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt1 = nums.count(1)
        if cnt1:
            return n - cnt1
        res = float("inf")
        for l in range(n):
            g = nums[l]
            for r in range(l + 1, n):
                g = self.gcd(g, nums[r])
                if g == 1:
                    res = min(res, r - l + (n - 1))
                    break
        
        return res if res != float("inf") else -1
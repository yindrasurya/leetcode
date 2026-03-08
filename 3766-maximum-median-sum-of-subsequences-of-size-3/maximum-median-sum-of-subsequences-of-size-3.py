class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        L, R = 0, len(nums)
        while L < R:
            L += 1
            R -= 2
            res += nums[R]
        return res
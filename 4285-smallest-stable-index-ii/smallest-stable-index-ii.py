class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minfromIndex = [0]*n
        minEle = float('inf')
        for i in range(n-1 ,-1 ,-1):
            minEle = min(minEle , nums[i])
            minfromIndex[i] = minEle
        maxEle = float('-inf')
        for i in range(0 , n):
            maxEle = max(maxEle , nums[i])
            minEle = minfromIndex[i]
            if maxEle - minEle <= k:
                return i

        return -1
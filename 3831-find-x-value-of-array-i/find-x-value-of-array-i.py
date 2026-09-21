class Solution:
    def resultArray(self, nums, k):
        result = [0]*k; cnt = [0]*k
        for num in nums:
            nc = [0]*k
            for v in range(k):
                nc[v*num%k] += cnt[v]
            nc[num%k] += 1
            for x in range(k): result[x] += nc[x]
            cnt = nc
        return result
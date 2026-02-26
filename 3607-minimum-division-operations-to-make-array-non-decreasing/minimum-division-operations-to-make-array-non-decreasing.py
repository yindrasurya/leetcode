class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0
        op = 0
        def giveMe(n):
            for i in range(2,int(sqrt(n))+1):
                if n % i == 0:
                    return n//i
            return 1
        n = len(nums)
        for i in range(n-1,0,-1):
            while nums[i-1] > nums[i]:
                ans = giveMe(nums[i-1])
                if ans == 1:
                    return -1
                nums[i-1] /= ans
                op += 1
        return op
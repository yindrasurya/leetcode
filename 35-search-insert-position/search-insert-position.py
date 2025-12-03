class Solution(object):
    def searchInsert(self, nums, target):
        length = len(nums)
        for i in range(length):
            if nums[i] >= target:
                return i
            
        return length
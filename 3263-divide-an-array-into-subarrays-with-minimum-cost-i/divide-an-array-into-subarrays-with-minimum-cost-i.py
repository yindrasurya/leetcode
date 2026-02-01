class Solution:
    def minimumCost(self, nums):
        firstMin = float('inf')
        secondMin = float('inf')

        for i in range(1, len(nums)):
            if nums[i] < firstMin:
                secondMin = firstMin
                firstMin = nums[i]
            elif nums[i] < secondMin:
                secondMin = nums[i]

        return nums[0] + firstMin + secondMin
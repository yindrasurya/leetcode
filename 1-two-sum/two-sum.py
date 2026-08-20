class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            required = target - num

            if required in seen:
                return [seen[required], i]

            seen[num] = i

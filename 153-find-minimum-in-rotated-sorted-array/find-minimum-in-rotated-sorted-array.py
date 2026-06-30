class Solution:
    def findMin(self, nums: List[int]) -> int:
        a=sorted(nums)
        return min(a)
        
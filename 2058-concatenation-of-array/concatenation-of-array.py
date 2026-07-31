class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n) :
            i=nums[i]
            nums.append(i)
        return nums
        


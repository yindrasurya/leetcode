class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curSum = 0
        for num in nums:
            curSum = ((curSum << 1) + num) % 5
            if curSum % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=0
        a=[]
        for i in nums:
            c+=i
            a.append(c)
        return a
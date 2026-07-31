class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        t=0
        for i in nums:
            t+=i
            a.append(t)
        return a
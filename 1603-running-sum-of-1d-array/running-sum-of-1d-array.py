class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        a.append(nums[0])
        for i in range(1,len(nums)):
            k=nums[i]+a[i-1]
            a.append(k)
        return a

            



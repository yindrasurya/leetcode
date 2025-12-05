class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix_sum = []
        suffix_sum = []
        pcs = 0
        scs = 0
        
        i = 0 
        while(i < len(nums)):

            pcs += nums[i]
            prefix_sum.append(pcs)

            scs += nums[len(nums) - 1 - i]
            suffix_sum.append(scs)
            i += 1
        
        suffix_sum.reverse()
        
        ans = 0
        i = 0
        while(i < len(nums) - 1):

            diff = prefix_sum[i] - suffix_sum[i + 1]
            if(diff % 2 == 0):
                ans += 1

            i += 1
        
        return ans 
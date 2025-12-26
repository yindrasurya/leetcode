class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        if k == len(nums): return max(nums)                     # case 1

        ctr = Counter(nums)

        if k == 1: return max((num for num in ctr               # case 2
                            if ctr[num] == 1), default = -1)    #

        ans = -1                                                #
        if ctr[nums[ 0]] == 1: ans = nums[0]                    # case 3
        if ctr[nums[-1]] == 1: ans =  max(ans, nums[-1])        #
        return ans                                              #
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findmin(nums):
            l,r=0,len(nums)-1
            if nums[l]<=nums[r]:
                return l
            while r-l!=1:
                mid=(l+r)//2
                if nums[mid]<nums[r]:
                    r=mid
                else:
                    l=mid
            return r
        min=findmin(nums)
        if target<=nums[-1]:
            l,r=min,len(nums)-1
        else:
            l,r=0,min
        while r>=l:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1
        
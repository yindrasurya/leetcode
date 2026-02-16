class Solution(object):
    def sortColors(self, nums: List[int]) -> None:
        def swap(a, b):
            a, b = b, a
            return a, b

        low = 0
        mid = 0
        high = len(nums) -1

        while (mid <= high):
            if nums[mid] == 2:
              nums[mid], nums[high] = swap(nums[mid], nums[high])
              high -= 1
            
            elif nums[mid] == 0:
                nums[mid], nums[low] = swap(nums[mid], nums[low])
                low += 1
                mid += 1
            
            elif nums[mid] == 1:
                mid += 1
        
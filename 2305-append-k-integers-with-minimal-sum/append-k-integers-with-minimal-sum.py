class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        nums.insert(0, 0)
        
        total = 0
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i - 1] - 1
            if gap > 0:
                count = min(k, gap)
                start = nums[i - 1] + 1
                end = start + count - 1
                total += (start + end) * count // 2
                k -= count
                if k == 0:
                    break

        if k > 0:
            start = nums[-1] + 1
            end = start + k - 1
            total += (start + end) * k // 2

        return total
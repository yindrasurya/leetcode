class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        size = len(nums)
        min_idx = 0
        max_idx = 0

        for i in range(size):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

        if min_idx < size // 2 and max_idx < size // 2:
            return max(min_idx, max_idx) + 1

        if min_idx >= size // 2 and max_idx >= size // 2:
            return max(size - min_idx, size - max_idx)

        if min_idx < size // 2 and max_idx >= size // 2:
            return min(
                min_idx + 1 + size - max_idx,
                min(size - min_idx, max_idx + 1)
            )

        return min(
            max_idx + 1 + size - min_idx,
            min(size - max_idx, min_idx + 1)
        )
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        max_heap = [-x for x in nums[:n]]
        heapify(max_heap)
        left_sum = sum(nums[:n])
        left_diff = [0] * (n + 1)
        left_diff[0] = left_sum

        for i in range(n, 2 * n):
            num = nums[i]
            if num < -max_heap[0]:
                left_sum += num + max_heap[0]
                heapreplace(max_heap, -num)
            left_diff[i - n + 1] = left_sum

        min_heap = nums[2 * n:]
        heapify(min_heap)
        right_sum = sum(min_heap)
        min_diff = left_diff[-1] - right_sum
        for i in range(2 * n - 1, n - 1, -1):
            num = nums[i]
            if num > min_heap[0]:
                right_sum += num - min_heap[0]
                heapreplace(min_heap, num)
            diff_index = i - n
            curr_diff = left_diff[diff_index] - right_sum
            min_diff = min(min_diff, curr_diff)
            
        return min_diff
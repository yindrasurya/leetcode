class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i = 0
        for j in range(n2):
            if nums1[i] > nums2[j]:
                i += 1
                if i >= n1:
                    break
        return max(j - i, 0)
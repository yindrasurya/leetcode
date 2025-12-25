# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower = 1
        upper = n
        ans = -1
        while lower <= upper:
            mid = (lower + upper) // 2
            if isBadVersion(mid):
                upper = mid - 1
                ans = mid
            else:
                lower = mid + 1
        return ans
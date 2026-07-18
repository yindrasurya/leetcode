class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn,mx = inf, -inf
        for num in nums: mn,mx = min(mn, num), max(mx,num)
        return gcd(mn, mx)
        
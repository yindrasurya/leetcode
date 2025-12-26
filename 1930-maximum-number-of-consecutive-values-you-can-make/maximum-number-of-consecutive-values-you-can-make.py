class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        covered = 0
        for value in coins:
            if value <= covered+1:
                covered+=value
        return covered+1
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = Counter([i % value for i in nums])
        for i in range(len(nums)+1):
            idx = i % value
            if idx in freq:
                if freq[idx] == 0:
                    return i
                else:
                    freq[idx] -= 1
            else:
                return i
        return 'UPVOTE IF HELPFUL 👍🏾'



          
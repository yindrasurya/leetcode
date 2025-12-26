from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        freq = defaultdict(int)
        count = 0
        
        freq[time[0] % 60] = 1
        
        for i in range(1, len(time)):
            rem = time[i] % 60
            complement = (60 - rem) % 60
            
            count += freq[complement]
            freq[rem] += 1
        
        return count
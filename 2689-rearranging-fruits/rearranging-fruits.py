class Solution:
    def minCost(self, basket1, basket2):
        freq = Counter(basket1)
        freq.subtract(basket2)
        min1 = min(freq)
        
        lst1 = []
        for key, value in freq.items():
            if value % 2 != 0:
                return -1
            for i in range(abs(value) // 2):
                lst1.append(key)
                
        lst1.sort()
        ans = 0
        for i in range(len(lst1) // 2):
            ans += min(lst1[i], min1 * 2)
        return ans
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i = j = k = 0
        for _ in range(n-1):
            next2 = ugly[i] * 2
            next3 = ugly[j] * 3
            next5 = ugly[k] * 5
            val = min(next3, next5, next2)
            ugly.append(val)
            if val == next2:
                i += 1
            if val == next3:
                j += 1
            if val == next5:
                k += 1
        return ugly[-1]
from functools import lru_cache

class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        digits = list(map(int, str(n)))[::-1]
        d = len(digits)

        def cntLengths(la, lb):
            @lru_cache(None)
            def dp(i, carry):
                if i == d:
                    return 1 if carry == 0 else 0
                t = digits[i]
                res = 0
                if i >= la:
                    rangeA = (0,)
                else:
                    rangeA = range(1, 10)
                if i >= lb:
                    rangeB = (0,)
                else:
                    rangeB = range(1, 10)
                for a in rangeA:
                    need = (t - carry - a) % 10
                    carryOut = (carry + a + need) // 10
                    if 0 <= need <= 9 and need in rangeB:
                        res += dp(i + 1, carryOut)
                return res

            return dp(0, 0)

        ans = 0
        for la in range(1, d + 1):
            for lb in range(1, d + 1):
                ans += cntLengths(la, lb)
        return ans
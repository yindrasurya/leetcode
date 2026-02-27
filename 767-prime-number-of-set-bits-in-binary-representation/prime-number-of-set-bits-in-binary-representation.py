class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        set_vals = {2, 3, 5, 7, 11, 13, 17, 19}
        ans = 0
        for i in range(left, right + 1):
            bits = 0
            num = i
            while num != 0:
                if (num & 1) != 0:
                    bits += 1
                num = num // 2
            if bits in set_vals:
                ans += 1
        return ans  
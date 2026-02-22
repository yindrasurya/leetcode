class Solution:
    def isHappy(self, n: int) -> bool:
        y = str(n)
        m = 0
        while m != 4:
            m = 0
            for x in y:
                m += int(x) ** 2
            if m == 1:
                return True
            y = str(m)
        return False
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []
        n = len(str(low))
        m = len(str(high))
        for length in range(n, m + 1):
            for i in range(10 - length):
                num = int(digits[i : i + length])
                if low <= num <= high:
                    res.append(num)
        
        return res
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a10 = int(a, 2)
        b10 = int(b, 2)

        sum10 = a10 + b10

        return bin(sum10)[2:]
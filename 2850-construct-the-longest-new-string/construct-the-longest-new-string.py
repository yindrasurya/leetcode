class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return 2*z + (min(x,y)*2 + 1)*2 if x != y else 2*z + (min(x,y)*2 )*2


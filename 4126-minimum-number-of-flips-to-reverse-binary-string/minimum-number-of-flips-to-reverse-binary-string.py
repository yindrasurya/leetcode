class Solution:
    def minimumFlips(self, n: int) -> int:

        # gets binary string
        binary_string: str = bin(n)[2:]

        flip_count: int = 0 

        # only traverses first half
        for i in range(len(binary_string) // 2): 
            
            if binary_string[i] != binary_string[-i - 1]: 
                flip_count += 2

        return flip_count
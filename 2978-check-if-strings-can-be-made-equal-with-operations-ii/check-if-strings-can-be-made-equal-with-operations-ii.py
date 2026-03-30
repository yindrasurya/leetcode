class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Extract even indices using slicing [::2] and odd using [1::2]
        # Sort them and compare
        even_match = sorted(s1[::2]) == sorted(s2[::2])
        odd_match = sorted(s1[1::2]) == sorted(s2[1::2])
        
        return even_match and odd_match
class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""
        for i in s:
            if i.isalnum():
                c=c+i.lower()
        l=0
        r=len(c)-1
        while l<r:
            if c[l]!=c[r]:
                return False
            l+=1
            r-=1
        return True
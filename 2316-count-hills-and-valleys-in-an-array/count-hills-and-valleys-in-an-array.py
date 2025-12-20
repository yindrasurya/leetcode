class Solution:
    def countHillValley(self, a: List[int]) -> int:
        b = (v for v,_ in groupby(a))
        res,l,m = 0,next(b,None),next(b,None)
        for r in b:
            res += l>m<r or l<m>r
            l,m = m,r
        
        return res
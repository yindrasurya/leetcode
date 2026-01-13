class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        check = lambda my,total=sum(l*l for _,_,l in a): \
            sum(l*min(my-y,l) for _,y,l in a if y<my)>=total/2
        return deque(takewhile(lambda p:sub(*p)>=1e-6,
            accumulate(count(),lambda q,_:check(m:=sum(q)/2) and (m,q[1]) or (q[0],m),
                initial=(max(y+l for _,y,l in a),0))),maxlen=1)[0][0]
class Solution:
    def minOperations(self, a: List[int], x: int) -> int:
        y = sum(a)-x
        d = {0:-1}|dict(zip(accumulate(a),count()))
        k = max(d[p]-d.get(p-y,inf) for p in d)
        return (-1,len(a)-k)[k>=0]
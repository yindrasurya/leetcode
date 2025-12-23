class Solution:
    def largestTriangleArea(self, a: List[List[int]]) -> float:
        return max(abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
            for (x1,y1),(x2,y2),(x3,y3) in combinations(a,3))
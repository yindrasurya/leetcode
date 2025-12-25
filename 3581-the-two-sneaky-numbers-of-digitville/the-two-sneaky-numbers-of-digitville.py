class Solution:
    def getSneakyNumbers(self, a: List[int]) -> List[int]:
        return nlargest(2,z:=Counter(a),z.get)
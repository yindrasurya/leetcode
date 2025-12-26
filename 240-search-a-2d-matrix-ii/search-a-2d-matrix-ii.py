class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target:
                return False
            for elem in row:
                if elem > target:
                    break
                if elem == target:
                    return True
        return False
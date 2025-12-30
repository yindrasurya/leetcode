class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        cols = set()
        pos_diagonal = set()
        neg_diagonal = set()

        def backtracking(r):
            if r == n:
                copy = []
                for row in board:
                    string = "".join(row)
                    copy.append(string)
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue
                
                board[r][c] = 'Q'
                cols.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)

                backtracking(r+1)

                # undo
                board[r][c] = '.'
                cols.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
        
        backtracking(0)
        return res

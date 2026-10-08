class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num ==".":
                    continue
                
                row_group = r // 3
                col_group = c // 3


                box = row_group * 3 + col_group

                if num in rows[r] or num in cols[c] or num in boxes[box]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

        return True 


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for i in range(9):
            for j in range(9):
                n = board[i][j]

                if n == ".":
                    continue
                
                row_key = (n, i, 'row')
                col_key = (n, j, 'col')
                box_key = (n, i//3, j//3, 'box')

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True
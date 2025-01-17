class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row
        for row in board:
            row = list(filter(lambda x: x != '.', row))
            if len(row) != len(set(row)):
                return False

        # Boxes
        grids = []
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                grid = []
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        grid.extend(board[r][c])
                print(grid)
                grids.append(grid)


        print(grids)
        for grid in grids:
            grid = list(filter(lambda x: x != '.', grid))
            if len(grid) != len(set(grid)):
                return False
        
        
        # Column
        board = list(map(list, zip(*board)))
        for col in board:
            col = list(filter(lambda x: x != '.', col))
            if len(col) != len(set(col)):
                return False

        return True
        
        
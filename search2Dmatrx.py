class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        target_row = 0
        row_end = matrix[target_row][col - 1]

        while row_end < target:
            target_row += 1
            if target_row < row:
                row_end = matrix[target_row][col - 1]
            else:
                return False

        left, right = 0, col-1

        while left <= right:

            mid = left + (right - left) // 2

            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False
            
        
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        height = len(mat)
        width = len(mat[0])
        visited = []

        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    visited.append((i,j))
                else:
                    mat[i][j] = "#"

        for row, col in visited:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                offRow = row + dx
                offCol = col + dy

                if 0 <= offRow < height and 0 <= offCol < width and mat[offRow][offCol] == "#":
                    mat[offRow][offCol] = mat[row][col] + 1
                    visited.append((offRow, offCol))

        return mat

        


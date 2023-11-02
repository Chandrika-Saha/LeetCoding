class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if (image[sr][sc] == color):
            return image
        
        maxRow = len(image) - 1
        maxCol = len(image[0]) - 1
        originalColor = image[sr][sc]
        self.dfs(image, sr, sc, maxRow, maxCol, originalColor, color)

        return image

    def dfs(self, image: List[List[int]], sr: int, sc: int, maxRow: int, maxCol: int, originalColor: int, newColor: int):

        if sr > maxRow or sr < 0 or sc > maxCol or sc < 0:
            return
        if image[sr][sc] != originalColor:
            return 
        
        image[sr][sc] = newColor

        self.dfs(image, sr - 1, sc, maxRow, maxCol, originalColor, newColor)
        self.dfs(image, sr + 1, sc, maxRow, maxCol, originalColor, newColor)
        self.dfs(image, sr, sc - 1, maxRow, maxCol, originalColor, newColor)
        self.dfs(image, sr, sc + 1, maxRow, maxCol, originalColor, newColor)


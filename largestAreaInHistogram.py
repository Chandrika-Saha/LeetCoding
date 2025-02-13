class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            index = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
            stack.append((index, h))


        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area

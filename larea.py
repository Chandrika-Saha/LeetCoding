    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while s and heights[s[-1]] >= h:
                ch = heights[s.pop()]
                l = s[-1] if s else -1
                w = i - l - 1
                max_area = max(max_area, ch * w)
            s.append(i)

        return max_area

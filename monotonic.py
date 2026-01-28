    def largestRectangleArea(self, heights: List[int]) -> int:

        maxarea = 0
        s = []

        for i, h in enumerate(heights):
            # This is the left boundary of the current height
            start = i

            # As long as we find a height that is less than the top height, we keep going
            # The idea is, we hit a bar that is lower than the last examined bar,
            # we simply need to calculate the area for the previous one since it cannot get 
            # higher than what it already had, we cannot extend it since we encountered a lower
            # bar.
            while s and s[-1][1] > h:
                idx, height = s.pop()
                maxarea = max(maxarea, height * (i - idx))
                # Since we are calculating the area with the bars that are higher than the current
                # one, we know we can extend the current bar to the left, hence we reset the left 
                # limit for the current bar
                start = idx

            s.append([start, h])
      
        # These are the leftover bars that go till the end of the height, because they were not popped.
        # We consider all of them for the maxarea.
        for i, h in s:
            maxarea = max(maxarea, h * (len(heights) - i))

        return maxarea


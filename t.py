def trap(self, height: List[int]) -> int:
        # Need the whole picture to porperly calculate the trapped water
        # Otherwise, there is a chance we might over or under calculate
        # Hence, this is a two pointer problem
        l, r = 0, len(height)-1
        lm, rm = 0, 0
        water = 0

        while l < r:
            rh, lh = height[r], height[l]
            # In case the left is less than right, we want to see how much we can capture on the left side first
            # To do that, we need the max height on the left side. 
            # We simply need to subtract the current height from the max left height to get the adjusted height for that left height
            # Append this to the current water calculation.
            if lh <= rh:
                lm = max(lh, lm)
                water += lm - lh
                l += 1
            else:
                # This is pretty much like the left side, only reversed, but the logic to calculate water on this side is the same as left. 
                # The thing is, if there is a right height that is lower than the left height, we try to approach towards left, the same but reversed logic with the left side. 
                # This way we make sure that we don't count the water that should not be counted because there's no max-right left...
                # And also, we make sure we do count the water for which there is an intermediate max right.
                rm = max(rh, rm)
                water += rm - rh
                r -= 1
                

        return water

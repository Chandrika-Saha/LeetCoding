class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        if len(height) <= 2:
            return 0
        
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        total = 0

        while left < right:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(height[left], maxLeft)
                total += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(height[right], maxRight)
                total += maxRight - height[right]

        return total

        
            


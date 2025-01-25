class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #----- Brute-force approach-----, time-limit exceeds

        # maxarea = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         curr_area = min(height[i], height[j]) * (j - i)
        #         maxarea = max(maxarea, curr_area)

        # return maxarea

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return max_area

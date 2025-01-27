class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        if len(height) <= 2:
            return 0


        left_max = []
        left_max.append(height[0])
        
        for i in range(1, len(height)):
            left_max.append(max(height[i], max(left_max)))


        right_max = []
        right_max.append(height[-1])

        for i in range(len(height) - 2, -1, -1):
            right_max.insert(0, max(height[i], max(right_max)))

        min_index = []
        for i in range(len(height)):
            min_index.append(min(left_max[i], right_max[i]))

        total = 0
        for i in range(1, len(height)-1):
            if min_index[i] - height[i] > 0:
                total += min_index[i] - height[i]

        return total





        
            


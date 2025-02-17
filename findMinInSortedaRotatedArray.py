class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #Initialize left and right pointers
        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        # Binary Search
        while left < right:
            # Calculate the mid index
            mid = left + (right - left) // 2

            # If the middle number is smaller than the right most number,
            # it means the list is sorted as far as we can see.
            # So we need to look at the earlier half of the array to find the minimum
            # We cannot exclude mid in this context since we also have to be sure if it's the lowest item or not
            if nums[mid] <= nums[right]:
                right = mid
            # Otherwise, it means we are at the end of the sorted list
            # or the rotation pushed the smaller items towards the end
            # so, we need to look for the min item near the end of the list
            else:
                left = mid + 1
            

        return nums[left]
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # --------------- SIMPLE SOLUTION --------------------
        # Create an array with all zeros with the same length
        result = [0] * len(nums)

        # For all numbers
        for num1 in nums:
            # Increment the index that corresponds to that numbers
            result[num1] += 1
            # If the count is more than 1, return that
            if result[num1] > 1:
                return num1
    
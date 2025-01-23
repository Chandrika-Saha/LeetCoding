class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
    	# Sort the numbers
        nums.sort()
        # Create the result list
        result_list = []

        # Iterate through all the numbers
        for i in range(len(nums)):
            # If same numbers, we can skip. Because the array is sorted
            # and we already found all possible combinations with the old number
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            # This part is basically two sum II, finding target in the sorted array
            left = i + 1
            right = len(nums) - 1

            # As long as the left is less than right
            while left < right:
                # Calculate 3 sum
                summation = nums[left] + nums[right] + nums[i]
                # If sum greater, decrement the right pointer to decrease the sum
                if summation > 0:
                    right -= 1
                # If sum lesser, increment the left pointer to increase the sum
                elif  summation < 0:
                    left += 1
                else:
                    # Match found, add it to the result list    
                    result_list.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # Now, move the left pointer
                    # Skip the same numbers since it was already considered once
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return result_list
                

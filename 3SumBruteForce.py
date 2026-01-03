class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Trying the brute-force approach, time-limit exceeded
        # Use three for loops
        result_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    addition = nums[i] + nums[j] + nums[k]
                    if addition == 0 and sorted([nums[i], nums[j], nums[k]]) not in result_list:
                        result_list.append(sorted([nums[i], nums[j], nums[k]]))

        return result_list
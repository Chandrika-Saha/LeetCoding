class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        result = len(nums)
        
        for i in range(result):
            result = result ^ i ^ nums[i]

        return result

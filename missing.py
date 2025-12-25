class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = len(nums)
        return (r * (r + 1))//2 - sum(nums)
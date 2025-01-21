class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                maxLength = max(length, maxLength)
        
        return maxLength
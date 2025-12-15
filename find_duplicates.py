class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        result = [n for n, c in counts.items() if counts[n] > 1]

        return result
        
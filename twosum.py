class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for index, number in enumerate(nums):
            
            difference = target - number

            if difference in mapping:
                return [mapping[difference], index]

            mapping[number] = index

        return

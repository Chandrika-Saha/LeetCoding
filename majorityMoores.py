class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # element, count = 0, 0
        # countAll = {}

        # for num in nums:
        #     countAll[num] = 1 + countAll.get(num, 0)
        #     if countAll[num] > count:
        #         element = num
        #         count = countAll[num]
        
        # return element

        element, count = 0, 0

        for num in nums:
            
            if count == 0:
                element = num

            count += (1 if element == num else -1)

        return element




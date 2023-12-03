class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort() #to avoid duplicated
        
        #iterate through nums
        for i , num in enumerate(nums):
            #checking for duplicates
            if i > 0 and num == nums[i - 1]:
                continue
            #2 pointers
            left, right = i + 1, len(nums) - 1

            while left < right: 
                threeSum = num + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    # -4, -1, -1, 0, 1, 2
                    #
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result


            



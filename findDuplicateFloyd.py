class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Floyds Tortoise-Hare algorithm

        slow, fast = 0, 0
        
        # First loop detects the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        # Second loop finds the entry point to the cycle
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
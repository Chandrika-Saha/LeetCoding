class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize the left and right pointers
        left = 0
        right = len(numbers) - 1

        # Run the loop till the end of the list
        while left < len(numbers) - 1:
            # Calculate the total of the two numbers
            total = numbers[left] + numbers[right]
            # If this total is less than target, that means we need to add onto the number
            # This would require us to increament the left pointer
            if total < target:
                left += 1
            # On the other hand, if we are exceeding the target, this means that we need to decreaset the total
            # This would require us to decreament the right pointer
            elif total > target:
                right -= 1
            # If they are equal, we have found our match, return left and right
            else:
                return [left+1, right+1]
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # If there's only one stone, we don't need to break it, just return that
        if len(stones) == 1:
            return stones[0]

        # Sort the list of stones in decending order
        stones.sort(reverse = True)

        # Go through the entire list while breaking stones, until you reach the last stone
        while len(stones) > 1:
            # Get the two biggest stones
            a = stones.pop(0)
            b = stones.pop(0)
            
            # If they are equal, result is 0, otherwise the abs of the difference
            result = 0 if a == b else abs(a - b)
            
            # Add the result to the list of stones and sort the list again
            stones.append(result)
            stones.sort(reverse = True)
            
        # Return the remaining stone, it's either going to be a difference or zero
        return stones[0]

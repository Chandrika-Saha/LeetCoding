class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert the numbers to neagatives so that the minheap can be treated as maxheap
        stones = [-s for s in stones]

        # Heapify the negative numbers list
        heapq.heapify(stones)

        # As long as there's one stone left
        while len(stones) > 1:
            # Get the first two biggest neg numbers
            big = heapq.heappop(stones)
            small = heapq.heappop(stones)
            # If the bigger number is smaller than the small number,
            # then add the negative difference between them to the tree
            if big < small:
                heapq.heappush(stones, big - small)

        # Add 0 to the list in case we broke all the stones
        stones.append(0)
        # Return the remaining stone
        return abs(stones[0])
class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0] * (n + 1)
        for i in range(1, n+1):
            counts[i] = counts[i >> 1] + (i & 1)

        return counts
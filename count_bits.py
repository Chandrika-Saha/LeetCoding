class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(n):
            count = 0
            while n != 0:
                n &= (n - 1)
                count += 1
            return count

        ans = []
        for i in range(0, n+1):
            ans.append(count_ones(i))

        return ans
        
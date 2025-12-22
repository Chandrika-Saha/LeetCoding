class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            # This line subtract one from the original number first,
            # then do a bit-wise and with the original number.
            # The subtract by 1 gets rid of 1 rightmost 1 at a time
            n &= (n - 1) 
            count += 1
        return count
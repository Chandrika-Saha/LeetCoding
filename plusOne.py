class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(n) for n in list(str(int(''.join([str(n) for n in digits])) + 1))]
        
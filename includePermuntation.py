class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l, r = 0, len(s1)
        while r < (len(s2) + 1):
            if sorted(s2[l:r]) == s1:
                return True
            else:
                l += 1
                r = l + len(s1)
        return False
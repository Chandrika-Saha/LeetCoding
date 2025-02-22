class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1

        char_so_far = []
        result = 1
        max_len = 0

        l, r = 0, 1
        while r < len(s):
            if s[l] != s[r] and s[r] not in char_so_far:
                result += 1
                char_so_far.append(s[r])
                r += 1
            else:
                char_so_far = []
                result = 1
                l += 1
                r = l + 1
            max_len = max(max_len, result)
            
    
        return max_len
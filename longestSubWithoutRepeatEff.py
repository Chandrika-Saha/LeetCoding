class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        char_dict = {}
        start = 0
        maxLength = 0

        for i in range(len(s)):
            if s[i] in char_dict and char_dict[s[i]] >= start:
                start = char_dict[s[i]] + 1
            maxLength = max(maxLength, i - start + 1)
            char_dict[s[i]] = i

        return maxLength

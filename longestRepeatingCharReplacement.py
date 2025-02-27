class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        maxLength = 0
        l = 0

        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            print(char_count)
            if (r - l + 1) - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)
        
        return maxLength


        
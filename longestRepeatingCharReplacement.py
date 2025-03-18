class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize dictionary to store the count of each characters
        char_count = {}
        maxLength = 0 # Maximum length so far
        l = 0 # Left pointer initialized to 0

        # For every index
        for r in range(len(s)):
            # Count up that specific character
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            
            # Getting the length of the substring
            # Subtracting it from the maximum occurring character count
            # Checking if this count is greater than k
            # Essentially, this condition is resetting the window because the length of the 
            # leftover strings has outgrown the value of k and so, there is a chance that the
            # another charcter might exist for maximum replacement.
            while (r - l + 1) - max(char_count.values()) > k:
                char_count[s[l]] -= 1 # Decreament the leftmost character count, since it's out of window
                l += 1 # increment the l pointer so that we can look for potential char that maximizes replacement

            # In the meantime, keep tracking the maximum substring with the repeating char replacement
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength


        
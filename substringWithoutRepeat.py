# Main objective of the solution is to reset the starting index once a repeating character is found
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If the given string has only one character
        if len(s) == 1:
            return 1
        # If the given string does not have any characters, no duplicates
        if len(s) == 0:
            return 0

        # dictionary to keep track of the indices of chars
        char_dict = {}
        start = 0 # Starting index
        maxLength = 0 # The maximum length so far

        # For all the indices of the string
        for i in range(len(s)):
            
            # If the current char exists in the dictionary and if it has an index of more than start,
            # that means the current char has been repeated and that needs to be considered when calculating
            # the max length
            if s[i] in char_dict and char_dict[s[i]] >= start:
                # Update the start to the next of the repeating character
                # This is done to find other substrings that might be longer
                start = char_dict[s[i]] + 1 
            
            # Maximum length so far. Either max length or,
            # the difference between start and current index
            maxLength = max(maxLength, i - start + 1)
            
            # Replace the index of every char with the current index
            # This will replace the index value of any repeating charcter to the curr index
            char_dict[s[i]] = i

        return maxLength


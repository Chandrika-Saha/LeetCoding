class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        reConstructed = ""

        for c in s:
            if c.isalnum():
                reConstructed += c.lower()

        return reConstructed == reConstructed[ : : -1]

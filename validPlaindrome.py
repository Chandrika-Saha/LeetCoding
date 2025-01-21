import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s.strip() == '':
            return True

        s = re.sub(r'[^a-z0-9]', '', s.strip().lower())
       
        return s == s[::-1]
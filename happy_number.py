class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while True: #n != 1 and n not in seen:
            # seen.add(n)
            n = sum(int(c) ** 2 for c in str(n))
          
            if n == 1:
                return True
            if n not in seen:
                seen.add(n)
            else:
                return False
            
        return n == 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # keep a carry and a sum (add)
        carry = 0
        add = ""
        aReverse, bReverse = a[::-1], b[::-1]

        for i in range(max(len(aReverse), len(bReverse))):
            aDigit = ord(aReverse[i]) - ord('0') if i < len(aReverse) else 0
            bDigit = ord(bReverse[i]) - ord('0') if i < len(bReverse) else 0

            total = aDigit + bDigit + carry
            char = str(total % 2)
            add = char + add

            carry = total // 2

        if carry:
            add = "1" + add
        
        return add

        

class Solution:

    def isValid(self, s: str) -> bool:

        m = {")": "(", "}": "{", "]": "["}
        st = set(m.values())
        l =[]

        for c in s:
            if c in st:
                l.append(c)
            if c in m:
                if not l:
                    return False
                if m[c] != l[-1]:
                    return False
                l.pop()

        return not l

#     def isValid(self, s: str) -> bool:
# 
#         stack = []
# 
#         bracketMap = {')' : '(', '}' : '{', ']' : '['}
# 
#         for c in s:
#             if c in bracketMap:
#                 if stack and stack[-1] == bracketMap[c]:
#                     stack.pop()
#                 else:
#                    return False 
#             else:
#                 stack.append(c)
# 
#         return True if not stack else False
        
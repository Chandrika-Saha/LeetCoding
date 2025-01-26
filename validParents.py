class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False

        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack:   
                    if stack[-1] == "(" and char == ")":
                        stack.pop()
                    elif stack[-1] == '{' and char == "}":
                        stack.pop()
                    elif stack[-1] == "[" and char == "]":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            
        return len(stack) == 0
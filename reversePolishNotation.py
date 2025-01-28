class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if t in "+-*/":
                num2, num1 = stack.pop(), stack.pop()
                result = self.calculate(int(num1), int(num2), t)
                stack.append(result)
            else:
                stack.append(t)
        
        return int(stack[0])

    def calculate(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == '-':
            return a - b
        elif operator == "*":
            return a * b
        else:
            return a // b if a * b >= 0 else -(-a // b)
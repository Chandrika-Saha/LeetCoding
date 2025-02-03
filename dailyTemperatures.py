class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if len(temperatures) == 1:
            return [0]


        result = [0] * len(temperatures)
        stack = [] # [temp, index]
        # 73 74 75 71
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, stackI = stack.pop()
                result[stackI] = i - stackI

            stack.append([t, i])

        return result




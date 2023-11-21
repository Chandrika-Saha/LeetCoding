class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        countDict = {}
        resultLength = 0

        # for char in s:
        #     countDict[char] = countDict.get(char, 0) + 1

        # for count in countDict.values():
        #     resultLength += (count // 2) * 2
        #     if (resultLength % 2) == 0 and (count % 2 == 1):
        #         resultLength += 1
        # print(Counter(s))
        
        for count in Counter(s).values():
            resultLength += (count // 2) * 2
            if (resultLength % 2) == 0 and (count % 2 == 1):
                resultLength += 1

        return resultLength

        

        


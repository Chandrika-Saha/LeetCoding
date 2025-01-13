class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # str_dict = defaultdict(list)

        # for word in strs:

        #     sorted_w = ''.join(sorted(word))
        #     str_dict[sorted_w].append(word)

        # return list(str_dict.values())

        str_dict = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord('a')] += 1
            
            str_dict[tuple(key)].append(s)

        return list(str_dict.values())



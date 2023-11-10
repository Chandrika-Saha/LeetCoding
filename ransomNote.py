class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # map_magazine = {}

        # for c in magazine:
        #     map_magazine[c] = map_magazine.get(c, 0) + 1

        map_magazine = Counter(magazine)

        for c in ransomNote:
            if map_magazine.get(c, 0) == 0:
                return False
            else:
                map_magazine[c] = map_magazine[c] - 1
        
        return True
        
            

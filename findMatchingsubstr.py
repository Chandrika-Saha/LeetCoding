class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1dict = Counter(s1)
        w = len(s1)
        s2dict = Counter(s2[:w])

        if s1dict == s2dict:
            return True

        for r in range(w, len(s2)):
            
            s2dict[s2[r]] += 1
            
            old = s2[r - w]
            s2dict[old] -= 1
            if s2dict[old] == 0:
                del s2dict[old]

            if s2dict == s1dict:
                return True

        return False

            

        

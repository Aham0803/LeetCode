from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1c = Counter(s1)
        s2c = Counter(s2[:n])

        if s1c == s2c:
            return True
        
        for i in range(n,len(s2)):
            s2c[s2[i]] += 1
            s2c[s2[i-n]] -= 1


            if s2c[s2[i-n]] == 0:
                del s2c[s2[i-n]]
            
            if s2c == s1c:
                return True
        return False
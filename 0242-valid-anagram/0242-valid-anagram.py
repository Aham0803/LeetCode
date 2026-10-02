class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # s = sorted(s)
        # t = sorted(t)
        # for i in range(len(s)):
        #     if(s[i] != t[i]):
        #         return False
        # return True

        if len(s) != len(t):
            return False
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0) + 1
        for ch in t:
            d[ch] = d.get(ch,0)-1
        
        for v in d.values():
            if v != 0:
                return False
        return True

 

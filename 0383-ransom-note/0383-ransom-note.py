class Solution:
    def canConstruct(self, s: str, t: str) -> bool:
        d = {}
        for ch in t:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for ch in s:
            if ch not in d:
                return False
            d[ch] -= 1
            if d[ch] < 0:
                return False
        return True
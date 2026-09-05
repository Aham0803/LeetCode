class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vo = "aeiou"
        v = 0
        c = 0
        for ch in s:
            if ch in vo:
                v += 1
            elif ch.isalpha():
                c += 1
        
        if c > 0:
            score = v // c
            return score
        return 0

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Base check: total items must match
        if len(pattern) != len(words):
            return False
            
        # The 3-way set check ensures a strict 1-to-1 bijection
        return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))

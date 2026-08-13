class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count ={}
        window ={}
        if len(p) > len(s):
            return []

        for ch in p:
            p_count[ch] = p_count.get(ch,0)+1

        result =[]
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r] , 0)+1

            if r-l+1 > len(p):
                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]

                l += 1

            if window == p_count:
                result.append(l)
        
        return result
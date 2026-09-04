class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = []
        for v in s:
            if v == y:
                ans.append(v)
        
        for v in s:
            if v != y:
                ans.append(v)
        return "".join(ans)
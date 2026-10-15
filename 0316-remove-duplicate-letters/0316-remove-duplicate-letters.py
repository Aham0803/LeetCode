class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        seen = set()
        count ={}
        for ch in s:
            count[ch] = count.get(ch,0)+1
        st = []
        seen = set()
        for c in s:
            count[c] -= 1
            if c in seen:
                continue
            while st and st[-1]> c and count[st[-1]]>0:
                # seen.remove(st.pop())
                seen.remove(st[-1])
                st.pop()
            st.append(c)
            seen.add(c)
        return "".join(st)
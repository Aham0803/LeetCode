class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        last ={c:i for i,c in enumerate(s)}

        for i , c in enumerate(s):
            if c in st:
                continue
            while st and st[-1]>c and last[st[-1]]>i:
                st.pop()
            st.append(c)
        return "".join(st)
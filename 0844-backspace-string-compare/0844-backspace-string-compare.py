class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s1 = []
        # t1 =[]
        # for i in range(len(s)):
        #     if s[i] == '#':
        #         if s1:
        #             s1.pop()
        #     else:
        #         s1.append(s[i])
        # for i in range(len(t)):
        #     if t[i] == '#':
        #         if t1:
        #             t1.pop()
        #     else:
        #         t1.append(t[i])
        # return s1 == t1

        def processed(string: str):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        return processed(s) == processed(t)

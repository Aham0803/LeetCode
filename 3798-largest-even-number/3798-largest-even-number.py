class Solution:
    def largestEven(self, s: str) -> str:
        # for i in range(len(s)-1 , -1 , -1):
        #     if int(s[i]) % 2 == 0:
        #         return s[:i+1]
        # return ""

        index  = -1
        n = len(s)
        for i in range(n-1 , -1,-1):
            val = int(s[i])
            if val % 2 == 0:
                index = i
                break
        return s[:index+1]

        
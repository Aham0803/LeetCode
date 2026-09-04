class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        N = len(s)
        flag = True
        for i in range(0,N-1):
            a = int(s[i])
            b = int(s[i+1])
            dif = abs(a-b)
            if dif > 2:
                flag = False
                break
        return flag
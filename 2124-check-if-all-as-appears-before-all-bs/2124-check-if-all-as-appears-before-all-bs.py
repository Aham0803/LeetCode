class Solution:
    def checkString(self, s: str) -> bool:
        '''
        need to find first occurence of b and last occurence of a
        if a < b return true
        '''
        # N = len(s)
        # lastA = -1
        # for i in range(0,N):
        #     if s[i] == 'a':
        #         lastA = i
        #     else:
        #         break
        
        # firstB = N

        return s.rfind("a")<s.find("b") or s.find("b") == -1
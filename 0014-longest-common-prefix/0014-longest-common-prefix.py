class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ans = strs[0]
        # for i in range(1,len(strs)):
        #     j =0 
        #     while(j < len(ans) and j < len(strs[i])):
        #         if ans[j] != strs[i][j]:
        #             break
        #         j += 1
        #     ans = ans[:j] 
        # return ans

        # if len(strs) == 0:
        #     return ""
        # result = ""
        # base = strs[0]
        # for i in range(len(base)):
        #     for word in strs[1:]:
        #         if i == len(word) or word[i] != base[i]:
        #             return result
        
        #     result += base[i]
        # return result
        
        N = len(strs[0])
        length = 0
        for i in range(0,N):
            check = strs[0][i]
            flag = True
            for v in strs:
                if len(v) <= i or v[i] != check:
                    flag = False
                    break
            
            if flag:
                length += 1
            else:
                break
        
        return strs[0][0:length]
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

        if len(strs) == 0:
            return ""
        result = ""
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return result
        
            result += base[i]
        return result
        
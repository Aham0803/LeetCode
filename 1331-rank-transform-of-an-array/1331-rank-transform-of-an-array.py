class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank = {}

        ans = []
        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i+1
        
        for i in arr:
            ans.append(rank[i])
        
        return ans

        
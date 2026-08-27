class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # row
        N = len(matrix) 
        # column 
        M = len(matrix[0])
        ans = []
        for j in range(0 , M):
            curr =[]
            for i in range(0 , N):
                curr.append(matrix[i][j])
            ans.append(curr)
        
        return ans
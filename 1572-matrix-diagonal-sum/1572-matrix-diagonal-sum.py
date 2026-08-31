class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        sumD = 0
        for i in range(0,N):
            sumD += mat[i][i]
        
        colLn = N-1
        # for i in range(0,N):
        #     sumD += mat[i][N-i-1]

        for i in range(0,N):
            sumD += mat[i][colLn]
            colLn -=1
        if N%2 != 0:
            mid = N//2
            sumD -= mat[mid][mid]
        return sumD
        
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(0, numRows):
            #row 1-- 1 col, row 2, -- 2 col
            cur = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(arr[i-1][j-1] + arr[i-1][j])
            arr.append(cur)
        return arr
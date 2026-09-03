class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = []
        for i in range(numRows):
            arr.append([])
        #print(arr)

        index,dir = 0, 1
        for v in s:
            arr[index].append(v)
            index += dir
            if index == numRows:
                dir = -1
                index = numRows - 2
            elif index == -1:
                dir = 1
                index = 1

        ans = ""
        for v in arr:
            ans += "".join(v)
        return ans

        
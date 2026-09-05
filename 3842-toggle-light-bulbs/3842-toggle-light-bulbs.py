class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        arr = [False]*101

        for v in bulbs:
            arr[v] = not arr[v]
        
        ans =[]
        for i in range(101):
            if arr[i]:
                ans.append(i)
        
        return ans
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        l = 0
        r= n-1 
        while(l < r):
            h = min(height[l] , height[r])
            wt =  r- l
            area = h * (r-l)
            ans = max(area , ans)
            
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return ans
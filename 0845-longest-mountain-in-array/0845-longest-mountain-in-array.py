class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(1,n-1):
            #  i ko peak maan
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                left = i
                right = i
                # left side decreasing he check kr
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1
                # right side dec h check kr
                while right < n-1 and arr[right] > arr[right+1]:
                    right += 1
                
                ans = max(ans , right-left+1)
    
        return ans
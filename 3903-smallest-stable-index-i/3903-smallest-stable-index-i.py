class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans = -1
        n = len(nums)
        for i in range(0,n):
            maxV = max(nums[0:i+1])
            minV = min(nums[i:])
            dif = maxV-minV
            if dif <= k:
                ans = i
                break
        return ans
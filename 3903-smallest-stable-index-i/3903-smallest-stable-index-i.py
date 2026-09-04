class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # ans = -1
        # n = len(nums)
        # for i in range(0,n):
        #     maxV = max(nums[0:i+1])
        #     minV = min(nums[i:])
        #     dif = maxV-minV
        #     if dif <= k:
        #         ans = i
        #         break
        # return ans

        ans = -1
        N = len(nums)
        def findMax(start, end):
            val = nums[start]
            for i in range(start, end+1):
                val = max(nums[i], val)
            return val
        def findMin(start, end):
            val = nums[start]
            for i in range(start, end+1):
                val = min(nums[i], val)
            return val
        for i in range(0, N):
            maxV = findMax(0,i)
            minV = findMin(i, N-1)
            dif = maxV - minV
            if dif <= k:
                ans = i
                break
        return ans
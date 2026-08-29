class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # nums.sort()
        # if len(nums) <= 2:
        #     return -1
        # else:
        #     return nums[1]

        # minV = nums[0]
        # maxV = nums[0]

        # for v in nums:
        #     minV= min(minV , v)
        #     maxV = max(maxV , v)
        
        minV = min(nums)
        maxV = max(nums)
        
        for v in nums:
            if v != minV and v != maxV:
                return v
        
        return -1
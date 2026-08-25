class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # currsum = 0
        # maxsum = float('-inf')
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         maxsum = max(sum , maxsum)
        # return maxsum

        currsum = nums[0]
        maxsum = nums[0]
        
        for i in range(1,len(nums)):
            currsum = max(nums[i] , currsum+nums[i])
            maxsum = max(maxsum, currsum)
        
        return maxsum
                
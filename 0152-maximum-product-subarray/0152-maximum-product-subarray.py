class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute forve
        # currprd = nums[0]
        # for i in range(len(nums)):
        #     prd = 1
        #     for j in range(i ,len(nums)):
        #         prd *= nums[j]
        #         currprd = max(prd,currprd)
        # return currprd

        currmax = nums[0]
        currmin = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            if num < 0:
                currmax , currmin = currmin , currmax
            currmax = max(num , currmax*num)
            currmin = min(num,currmin*num)

            ans = max(ans, currmax)
        
        return ans

        # optimal

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first approch
        # n = len(nums)
        # leftprd = [1]*n
        # rightprd = [1]*n
        # for i in range(1, len(nums)):
        #     leftprd[i] = leftprd[i-1] * nums[i-1]
        # for i in range(len(nums)-2 , -1 , -1):
        #     rightprd[i] *= rightprd[i+1] * nums[i+1]
        # ans = []
        # for i in range(len(nums)):
        #     ans.append(leftprd[i]*rightprd[i])
        # return ans

        # second approch
        # prefix = [1]*len(nums)
        # for i in range(1 , len(nums)):
        #     prefix[i] = nums[i-1] * prefix[i-1]
        # suffix = [1]*len(nums)
        # for i in range(len(nums) -2 , -1 , -1):
        #     suffix[i] = nums[i+1] * suffix[i+1]
        # ans =[1]*len(nums)
        # for i in range(len(nums)):
        #     ans[i] = prefix[i]*suffix[i]
        # return ans

        n = len(nums)
        ans = [1] * n
        # 1. Calculate left products and store them in ans
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        # 2. Calculate right products on the fly and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
        return ans
            
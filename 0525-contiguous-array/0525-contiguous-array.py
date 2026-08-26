class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # n = len(nums)
        # ans = 0
        # for i in range(len(nums)):
        #     zero = 0
        #     one = 0
        #     for j in range(i,n):
        #         if nums[j] == 0:
        #             zero += 1
        #         else:
        #             one += 1
        #         if zero == one :
        #             ans = max(ans , j-i+1)
        # return ans
            
        # optimal
        prefix = 0
        ans = 0

        first = {0: -1}

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in first:
                ans = max(ans, i - first[prefix])
            else:
                first[prefix] = i

        return ans

        
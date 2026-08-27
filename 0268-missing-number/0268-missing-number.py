class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        # optimal best
        n = len(nums)
        ans = n

        for i in range(n):
            ans = ans ^ i ^ nums[i]

        return ans
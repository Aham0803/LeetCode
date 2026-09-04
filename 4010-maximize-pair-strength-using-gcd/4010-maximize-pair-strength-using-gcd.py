class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range( 0, N):
            for j in range(i+1 , N):
                g = gcd(nums[i] , nums[j])
                ans = max(ans , nums[i]*nums[j] // (g*g))
        return ans
        
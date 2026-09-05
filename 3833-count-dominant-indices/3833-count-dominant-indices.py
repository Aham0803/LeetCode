class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)
        # for i in range(len(nums)-1):
        #     sum , count = 0 , 0
        #     for j in range(i+1 , n):
        #         sum += nums[j]
        #         count += 1
        #     avg = sum / count
        #     if avg < nums[i]:
        #         ans +=1
        # return ans

        total = sum(nums)
        count = N
        for i in range(N-1):
            total -= nums[i]
            count -= 1
            if nums[i] > total / count:
                ans += 1
        return ans

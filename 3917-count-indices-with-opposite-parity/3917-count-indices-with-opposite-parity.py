class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        ans = []
        N = len(nums)
        for i in range(0,N):
            count = 0
            for j in range(i+1 , N):
                if nums[i] % 2 != nums[j]%2:
                    count += 1
            ans.append(count)
        return ans
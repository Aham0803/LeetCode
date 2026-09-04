class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        # ans = []
        # N = len(nums)
        # for i in range(0,N):
        #     count = 0
        #     for j in range(i+1 , N):
        #         if nums[i] % 2 != nums[j]%2:
        #             count += 1
        #     ans.append(count)
        # return ans

        # three computatiion use
        odd , even = 0 , 0
        for v in nums:
            if v%2 == 0:
                even += 1
            else:
                odd += 1
        ans = []
        for v in nums:
            if v%2 != 0:
                ans.append(even)
                odd -= 1
            else:
                ans.append(odd)
                even -= 1
        return ans


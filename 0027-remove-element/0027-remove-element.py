class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return len(nums)

        nums[:] = [x for x in nums if x != val]
        return len(nums)

        # k = 0
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         count += 1
        #         k += 1
        # return count
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos =[]
        neg =[]
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range(len(pos)):
            nums[i*2] = pos[i]
            nums[(i*2)+1] = neg[i]
        return nums
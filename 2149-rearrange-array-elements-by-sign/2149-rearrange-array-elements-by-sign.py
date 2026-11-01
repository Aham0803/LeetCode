class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # brute force
        # pos =[]
        # neg =[]
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i])
        # for i in range(len(pos)):
        #     nums[i*2] = pos[i]
        #     nums[(i*2)+1] = neg[i]
        # return nums
        n = len(nums)
        result = [0]*n
        pos = 0 
        neg = 1
        for i in range(len(nums)):
            if nums[i]>0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2
        return result


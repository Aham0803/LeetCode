class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # increasing = True
        # decreasing = True
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         increasing = False     
        #     if nums[i] < nums[i+1]:
        #         decreasing = False
        # return increasing or decreasing

        N = len(nums)
        def isIncreasing():
            flag = True
            for i in range(1, N):
                if nums[i] < nums[i-1]:
                    flag = False
            return flag
        def isDecreasing():
            flag = True
            for i in range(1, N):
                if nums[i] > nums[i-1]:
                    flag = False
            return flag
        return isIncreasing() or isDecreasing()
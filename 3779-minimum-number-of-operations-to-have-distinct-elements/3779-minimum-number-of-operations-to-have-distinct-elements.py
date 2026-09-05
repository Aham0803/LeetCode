class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # wrong
        # num = nums[2:]
        # if len(nums) == 1:
        #     return 0
        # elif len(nums) < 3:
        #     return 1
        # elif len(num) <= 3:
        #     return 0
        # else:
        #     return 1

        """
        3,8,3,6,5,8 --> 3,6,5,8
        """
        operation = 0
        N = len(nums)
        lookup = set()
        for i in range(N-1,-1,-1):
            if nums[i] in lookup:
                operation = (i // 3) + 1 # 1 
                break
            lookup.add(nums[i])
        return operation
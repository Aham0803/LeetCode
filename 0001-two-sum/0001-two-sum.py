class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # m={}
        # for i in range(0,len(a)):
        #     part=target-a[i]
        #     if part in m:
        #         return [m[part],i]
        #     m[a[i]]=i

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
        
        
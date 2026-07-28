class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        ans = True
        if(len(nums)) == 1:
            ans = False
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                ans = True
                break
            else:
                ans = False   
        return ans 
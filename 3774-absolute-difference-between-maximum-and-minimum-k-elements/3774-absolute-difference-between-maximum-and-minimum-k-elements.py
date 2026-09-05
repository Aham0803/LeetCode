class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        return sum(nums[n-k:n]) - sum(nums[0:k])
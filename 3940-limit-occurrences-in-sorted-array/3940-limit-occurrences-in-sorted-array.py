class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = []
        
        for v in nums:
            if ans.count(v) < k:
                ans.append(v)
        return ans
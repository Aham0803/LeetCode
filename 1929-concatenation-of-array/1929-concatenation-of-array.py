class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        N = len(nums)
        for _ in range(2):
            for i in range(0,N):
                ans.append(nums[i])
        
        return ans
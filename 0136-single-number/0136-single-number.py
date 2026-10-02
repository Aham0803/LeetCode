class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq ={}
        for ch in nums:
            freq[ch] = freq.get(ch,0)+1
        val = list(freq.items())
        for i,j in val:
            if j == 1:
                return i
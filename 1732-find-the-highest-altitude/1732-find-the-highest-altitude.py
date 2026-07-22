class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        ans = 0
        for i in range(len(gain)):
            sum += gain[i]
            ans = max(ans , sum)
        return ans
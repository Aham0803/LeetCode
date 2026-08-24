class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        i = 0
        for j in range(1,len(prices)):
            if prices[i] > prices [j]:
                i = j
            sum = prices[j] -prices[i]
            ans = max(sum , ans)
            
        return ans



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ans = 0
        # i = 0
        # for j in range(1,len(prices)):
        #     if prices[i] > prices [j]:
        #         i = j
        #     sum = prices[j] -prices[i]
        #     ans = max(sum , ans)
        # return ans

        min_price = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            ans = max(ans, profit)

            min_price = min(min_price, prices[i])

        return ans



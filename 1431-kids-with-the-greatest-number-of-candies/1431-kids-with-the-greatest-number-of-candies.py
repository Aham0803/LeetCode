class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        large = max(candies)
        ans =[]

        for i in range(len(candies)):
            if candies[i]+ extraCandies >= large:
                ans.append(True)
            else:
                ans.append(False)
        return ans
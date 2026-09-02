class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        N = len(heights)
        expected.sort()
        count = 0
        for i in range(N):
            if expected[i] != heights[i]:
                count += 1
        return count
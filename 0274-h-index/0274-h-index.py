class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        n = len(citations)
        ans = 0
        for i in range(len(citations)):
            if citations[i] >=n-i:
                return n-i
        return 0
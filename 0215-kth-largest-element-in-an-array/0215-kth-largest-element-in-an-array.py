import heapq
class Solution:
    def findKthLargest(self, a: list[int], k: int) -> int:
        # minh = []
        # for n in a:
        #     heapq.heappush(minh , n)
        #     if len(minh) > k:
        #         heapq.heappop(minh)
        # return minh[0]
        return sorted(a)[-k]
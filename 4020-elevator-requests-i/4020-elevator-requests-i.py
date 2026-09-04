class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        N = len(requests)
        ans = requests[0]
        for i in range(0,N-1):
            ans += abs(requests[i] - requests[i+1])
        return ans
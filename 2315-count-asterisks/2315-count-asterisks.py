class Solution:
    def countAsterisks(self, s: str) -> int:
        print(s.split("|"))
        def countAsterisks(ss):
            return ss.count("*")
        arr = s.split("|")
        count = 0
        N = len(arr)
        count = 0
        for i in range(0,N,2):
            count += countAsterisks(arr[i])
        return count
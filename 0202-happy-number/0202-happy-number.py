class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            n = sum(int(c)**2 for c in str(n))
        return n == 1
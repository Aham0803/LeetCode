from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = sum(s==g for s,g in zip(secret,guess))

        total = sum((Counter(secret)&Counter(guess)).values())

        bulls = total - cows

        return f"{cows}A{bulls}B"
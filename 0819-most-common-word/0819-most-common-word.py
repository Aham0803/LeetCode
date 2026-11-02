import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = re.findall(r'[a-z]+', paragraph.lower())

        banned = set(banned)

        freq = Counter()

        for word in words:
            if word not in banned:
                freq[word] += 1

        return max(freq, key=freq.get)
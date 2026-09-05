class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        s ="zyxwvutsrqponmlkjihgfedcba"
        ans = ""
        def findWeight(word):
            val = 0
            for w in word: # c --> 99 - 97 = 2
                index = ord(w) - ord('a')
                val += weights[index]
            return val%26
        for word in words:
            val = findWeight(word)
            ans += s[val]
        return ans
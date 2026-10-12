class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        # Precompute character sets for each word to make intersection checks fast
        masks = [set(word) for word in words]
        max_val = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the two words share any common characters
                if not (masks[i] & masks[j]):
                    max_val = max(max_val, len(words[i]) * len(words[j]))
        return max_val


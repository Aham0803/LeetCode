class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        # Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort characters by frequency
        arr = list(freq.items())
        arr.sort(key=lambda x: x[1], reverse=True)

        # Build answer
        ans = ""

        for ch, count in arr:
            ans += ch * count

        return ans
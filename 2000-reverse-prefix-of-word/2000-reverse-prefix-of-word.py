class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # for i in range(len(word)):
        #     if word[i] == ch:
        #         return word[:i+1][::-1] + word[i+1:]
        # return word

        word = list(word)
        def reverse(start, end):
            while start < end:
                word[start], word[end] = word[end], word[start]
                start += 1
                end -= 1
        index = -1
        N = len(word)
        for i in range(0, N):
            if word[i] == ch:
                index = i
                break
        reverse(0, index)
        return "".join(word)


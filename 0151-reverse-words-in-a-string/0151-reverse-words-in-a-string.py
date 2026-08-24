class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split()
        # words.reverse()
        # return " ".join(words)

        words = []
        word =""

        for ch in s :
            if ch != " ":
                word += ch
            elif word:
                words.append(word)
                word =""
        
        if word :
            words.append(word)
        
        left = 0
        right = len(words)-1

        while left < right:
            words[left] , words[right] = words[right] , words[left]
            left += 1
            right -= 1
        
        return " ".join(words)
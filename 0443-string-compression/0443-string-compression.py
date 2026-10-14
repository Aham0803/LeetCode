class Solution:
    def compress(self, chars: list[str]) -> int:
        arr = []
        n = len(chars)
        i = 0
        while i < n:
            j = i
            while j < n and chars[i] == chars[j]:
                j += 1
            arr.append(chars[i])
            count = j-i
            if count > 1:
                for digit in str(count):
                    arr.append(digit)
            i = j
        
        for i in range(len(arr)):
            chars[i] = arr[i]
        return len(arr)

class Solution:
    def compress(self, chars: list[str]) -> int:
        arr = []
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and  chars[j] == chars[i]:
                j += 1
            arr.append(chars[i])
            count = j- i
            if count > 1:
                for digit in str(count):
                    arr.append(digit)
            i = j
        for i in range(len(arr)):
            chars[i] = arr[i]
        return len(arr)

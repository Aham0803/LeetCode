class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore
        # candidate = 0
        # count = 0
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate

        freq ={}
        for ch in nums:
            freq[ch] = freq.get(ch,0)+1
        
        # val = list(freq.items())
        # val.sort(key = lambda x:x[1] , reverse = True)
        # return val[0][0]
        return max(freq, key = freq.get)
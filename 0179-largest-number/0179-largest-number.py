from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        str_arr = [str(x)for x in nums]
        def compare(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0

        str_arr.sort(key = cmp_to_key(compare))
        ans = "".join(str_arr)
        if ans[0] == '0':
            return '0'
        return ans
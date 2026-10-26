class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # s = set(nums1) & set(nums2)
        # ans = []
        # for _ in range(2):
        #     ans.append([])
        
        # for num in set(nums1):
        #     if num not in s:
        #         ans[0].append(num)
        # for num in set(nums2):
        #     if num not in s:
        #         ans[1].append(num)
        # return ans


        # optimal
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
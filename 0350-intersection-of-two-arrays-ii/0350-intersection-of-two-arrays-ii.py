class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for n in nums2:
            if n in nums1:
                res.append(n)
                nums1.remove(n)
        return res

# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = k%len(nums)
#         left = 0
#         right = len(nums)-k

#         for i in range(k):
#             nums[left] , nums[right]= nums[right] , nums[left]
#             left += 1
#             right += 1
        
#         if len(nums) %2 != 0:
#             nums[k:] = sorted(nums[k:])
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # k = k % len(nums)

        # # reverse whole array
        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1
        #     right -= 1

        # # reverse first k
        # left = 0
        # right = k - 1

        # while left < right:
        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1
        #     right -= 1

        # # reverse remaining
        # left = k
        # right = len(nums) - 1

        # while left < right:
        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1
        #     right -= 1

        # by slicing

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]














        
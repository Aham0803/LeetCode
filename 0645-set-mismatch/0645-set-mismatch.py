class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = []
        s = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in s:
                arr.append(i)

        for num in nums:
            if nums.count(num) > 1:
                arr.insert(0, num)
                break

        return arr
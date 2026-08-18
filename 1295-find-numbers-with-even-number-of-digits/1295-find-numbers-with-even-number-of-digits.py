class Solution:
    # def c(self,n):
    #         count = 0
    #         while(n>0):
    #             n = n//10
    #             count += 1
    #         return count
    def findNumbers(self, nums: List[int]) -> int:
        
        # count = 0
        # for i in range(len(nums)):
        #     if self.c(nums[i]) % 2 == 0:
        #         count += 1
            
        # return count
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) %2 == 0:
                count +=1
        return count
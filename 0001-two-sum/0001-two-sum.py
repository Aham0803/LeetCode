class Solution:
    def twoSum(self, a: list[int], target: int) -> list[int]:
        m={}
        for i in range(0,len(a)):
            part=target-a[i]
            if part in m:
                return [m[part],i]
            m[a[i]]=i
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans =[]
        for start , end in intervals:
            if end < newInterval[0]:
                ans.append([start,end])
            elif start > newInterval[1]:
                ans.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval[0] = min(newInterval[0] , start)
                newInterval[1] = max(newInterval[1] , end)
        ans.append(newInterval)
        return ans




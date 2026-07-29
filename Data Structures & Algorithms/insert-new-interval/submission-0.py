class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0: 
            return [newInterval]
        
        newStart = newInterval[0]
        newEnd = newInterval[1]

        # Binary Search to find the first start that is < than us 
        l, r = 0, n - 1
        while (l <= r): 
            mid = (l + r) // 2
            currStart = intervals[mid][0]

            if newStart > currStart: 
                l = mid + 1
            else:
                r = mid - 1
        intervals.insert(l, newInterval)
        res = []
        for start,end in intervals: 
            if res and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start,end])
            
        return res

       
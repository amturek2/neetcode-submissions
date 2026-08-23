class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        count = 0 
        intervals.sort(key= lambda x:x[0])

        out = [intervals[0]]
        i = 1
        while i < len(intervals): 

            if out[-1][1] > intervals[i][0]:
                count += 1

                out[-1][1] =  min(out[-1][1], intervals[i][1])
            else: 
                out.append(intervals[i])
            i += 1
        
        return count
        
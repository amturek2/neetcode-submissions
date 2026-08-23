class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1: 
            return intervals


        inter = sorted(intervals, key = lambda x:x[0])
        res = [inter[0]]

        i = 1
        while i < n: 
            merge = False

            while i < n and res[-1][1] >= inter[i][0]:
                merge = True
                res[-1][1] = max(res[-1][1], inter[i][1])
                i += 1

            if not merge: 
                res.append(inter[i])
                i+=1
        return res
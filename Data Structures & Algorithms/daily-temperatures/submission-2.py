class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # want this to be strictly decreasing 
        res = [0 for i in range(n)] 

        stack = []
        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                tmp, curr_indx = stack.pop()
                res[curr_indx] = i - curr_indx
            stack.append((temperatures[i], i))

        return res
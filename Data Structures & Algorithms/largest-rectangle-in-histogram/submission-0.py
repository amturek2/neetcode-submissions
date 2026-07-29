class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        store = [[0, n] for _ in range(n)]

        # LEFT PASS 
        leftStack = []
        for i in range(n):
            while leftStack and heights[i] <= heights[leftStack[-1]]: 
                leftStack.pop()

            if leftStack: 
                store[i][0] = leftStack[-1]
            else: 
                store[i][0] = -1
            
            leftStack.append(i)
        
        # RIGHT PASS
        rightStack = []
        for i in range(n-1, -1, -1): 
            while rightStack and heights[i] <= heights[rightStack[-1]]: 
                rightStack.pop()
            
            if rightStack: 
                store[i][1] = rightStack[-1]
            else: 
                store[i][1] = n

            rightStack.append(i)

        # FINAL PASS
        maxx = -1 
        for i in range(n):
            l, r = store[i]
            area = (r - (l + 1)) * heights[i]
            maxx = max(maxx, area)
            


        return maxx
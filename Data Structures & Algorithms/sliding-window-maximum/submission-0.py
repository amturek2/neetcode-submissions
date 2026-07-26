class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq



        res = []

        l, r = 0, k -1 

        windowMaxes = []
        for i in range(0,k-1):
            heapq.heappush(windowMaxes, (-nums[i], i))

        while r < len(nums):
            # add the new number
            heapq.heappush(windowMaxes, (-nums[r], r))

            # print(f"l {l} r {r} windows heap {windowMaxes}")

            n_num, idx = windowMaxes[0]
            if l <= idx <= r: 
                res.append(-n_num)
            else: 
                while windowMaxes and windowMaxes[0][1] < l: 
                    # print(f"processing.... {windowMaxes}")
                    heapq.heappop(windowMaxes)
                
                res.append(-windowMaxes[0][0])
            
            # print(f"windowMaxes after {windowMaxes}")


            l += 1
            r += 1


        
        return res
        

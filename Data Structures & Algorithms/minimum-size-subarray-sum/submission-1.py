class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # so for this --> brute force is to go through all the subarrays in O(n^2)

        # [2,1,5,1,5,3]
        if (nums[0] >= target): 
            return 1
            
        n = len(nums)
        l, r = 0, 1

        summ = nums[0]
        minn_length = float('inf')

        while (l < n and r < n): 
            summ += nums[r]


            if (summ >= target): 
                minn_length = min(minn_length, (r - l + 1))
                if nums[l] < nums[r]: 
                    summ -= nums[l]
                    summ -= nums[r]
                    l += 1
                    continue 
            
    
            r += 1

        if minn_length == float('inf'): 
            return 0 
        return minn_length



            



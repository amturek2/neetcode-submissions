class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1: 
            return nums[0]
        def house(l, r): 

            n = r - l + 1
            dp = [0]* (r + 3)
            # print("called house",l, r, dp)

            while r >= l:
                take = nums[r] + dp[r + 2]
                skip = dp[r + 1]
                dp[r] = max(take,skip)
                r-= 1
                # print("dp", dp)
            return dp[l]
        
        allowFirst = house(0,length - 2)
        disableFirst = house(1,length - 1)

        return max(allowFirst,disableFirst)
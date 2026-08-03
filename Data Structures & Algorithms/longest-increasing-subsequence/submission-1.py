class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if the next one is greater - we can take it and track that next greater or we can use the one before 
        n = len(nums)
        dp = [1] * n
        
        # look if less than 
        for i in range(n-1, -1, -1): 
            for j in range(i+1, n): 
                if (nums[j] > nums[i]):
                    take = dp[j] + 1
                    dp[i] = max(take, dp[i])

        return max(dp)
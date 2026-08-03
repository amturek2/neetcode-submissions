class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}


        def backtrack(i, summ) -> int : 
            if i == n and summ == target: 
                return 1
            elif i == n: 
                return 0 

            if (i, summ) in memo: 
                return memo[(i,summ)]
            
            add = backtrack(i + 1, summ + nums[i])
            subtract = backtrack(i + 1, summ - nums[i])
            memo[(i, summ)] = add + subtract
            return memo[(i, summ)] 


        backtrack(0,0)
        print(memo)
        return  memo[(0,0)]
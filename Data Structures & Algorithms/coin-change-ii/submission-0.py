class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}
        def backtrack(i, amnt):
            if amnt == 0: 
                # count += 1
                return 1
            if i >= len(coins):
                return 0
            
            # keep taking that coin 
            if coins[i] > amnt: 
                return 0    
            
            if (i,  amnt - coins[i]) not in memo:
                memo[(i,  amnt - coins[i])] = backtrack(i, amnt - coins[i])
            if (i + 1, amnt) not in memo:
                memo[(i + 1, amnt)] = backtrack(i + 1, amnt)



            return memo[(i,  amnt - coins[i])] + memo[(i + 1, amnt)]
            # update and take next coin
            
     



        
        
        return backtrack(0,amount)
        
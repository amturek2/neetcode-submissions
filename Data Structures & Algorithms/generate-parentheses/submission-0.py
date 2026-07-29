class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # you have opens and n closes
        # in each scenario you can essentially add another parenthes

        # you have a choice to put the 

        # ( 
        # (  ( 
        res = []
        
        def recurseParen(open, close, current):

            if open == 0 and close == 0: 
                res.append(current)
                return 
            
            if close < open: 
                return 
            
            if open == 0: 
                return recurseParen(open, close -1, current + ')')
                 

            # if current[-1] == '(': 
            recurseParen(open - 1, close, current + '(' )
            recurseParen(open, close - 1, current + ')')



        recurseParen(n-1, n, "(")

        return res
        

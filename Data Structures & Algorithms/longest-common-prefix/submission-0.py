class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        strs = sorted(strs, key= lambda x: len(x))
        res = []
        for i in range(len(strs[0])): 
            curr_char = strs[0][i]
            for s in strs[1:]: 
                if s[i] != curr_char: 
                    return "".join(res)
            res.append(curr_char)
    
        return "".join(res)

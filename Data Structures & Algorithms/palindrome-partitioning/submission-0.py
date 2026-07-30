class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # try to evaluate each character as a center 
        n = len(s)
        res = []

        def inBounds(index):
            return (0 <= index < n)

        def isPalindrome(substring):
            n = len(substring)
            if n % 2 == 0: 
                l, r = (n // 2) - 1, (n// 2)
                while l >= 0 and r < n: 
                    if substring[l] != substring[r]:
                        return False
                    l -= 1
                    r += 1
            else: 
                l, r = (n // 2) - 1, (n// 2) + 1
                while l >= 0 and r < n: 
                    if substring[l] != substring[r]:
                        return False
                    l -= 1
                    r += 1
            return True
               
                

        def backtrack(start, curr):
            if start == n:
                res.append(curr.copy())
                return

            for end in range(start, n):
                substring = s[start:end + 1]
                if isPalindrome(substring):
                    curr.append(substring)
                    backtrack(end + 1, curr)
                    curr.pop()


        
        backtrack(0,[])

        return res
        
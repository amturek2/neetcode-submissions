class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        # keep a count of each specific num - if a num hits that constraint - we can return it -- this is O(n)
        count_dict = {}
        for val in nums: 
            
            count_dict[val] = count_dict.get(val, 0) + 1

            if count_dict[val] > (n//2): 
                return val
        
        return 
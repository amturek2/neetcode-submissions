class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # n = len(nums)
        # # keep a count of each specific num - if a num hits that constraint - we can return it -- this is O(n)
        # count_dict = {}
        # for val in nums: 
            
        #     count_dict[val] = count_dict.get(val, 0) + 1

        #     if count_dict[val] > (n//2): 
        #         return val
        
        # return 

        n = len(nums)
        if (n == 1): 
            return nums[0]
        nums.sort()

        currNum, currCount = nums[0], 1

        for i in range(1, n):

            if nums[i] != currNum: 
                currNum, currCount = nums[i], 1
            else: 
                currCount += 1
                if (currCount > (n//2)): 
                    return currNum 
        return 


    

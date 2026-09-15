class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0 
        while (i < n):
            j = i + 1
            # print(f"before with {i} ,{j} and nums = {nums}")
            while (j < n): 
                if (nums[i] > nums[j]): 
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp 
                j += 1
                # print(f"after with {i} ,{j} and nums = {nums}")

            i += 1
        
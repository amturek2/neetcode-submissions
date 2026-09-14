class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        # merge sort - O(nlogn)
        # breaks down every 
        
        # recursively break down, then merge the two back together 
        def merge(arr1, arr2): 
            res = []
            l, r = 0,0
            while l < len(arr1) or r < len(arr2): 
                if l >= len(arr1): 
                    while (r < len(arr2)): 
                        res.append(arr2[r])
                        r+= 1
                elif r >= len(arr2): 
                    while (l < len(arr1)): 
                        res.append(arr1[l])
                        l+= 1
                
                elif arr1[l] < arr2[r]:
                    res.append(arr1[l])
                    l += 1
                else: 
                    res.append(arr2[r])
                    r += 1

            return res 
            

        def mergesort(arr, l, r): 
            mid = (r + l) // 2
            if l == r: 
                return arr[l:r+1]
            
            arr1 = mergesort(arr, l, mid)
            arr2 = mergesort(arr, mid + 1, r)

            return merge(arr1, arr2)

            
        
        return mergesort(nums, 0, len(nums) - 1)




        
 
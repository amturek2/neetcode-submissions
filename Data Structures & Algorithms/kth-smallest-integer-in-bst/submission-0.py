# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        step = 0 
        res = None

        def dfs(root):
            nonlocal step
            nonlocal res
            if not root: 
                return 

            dfs(root.left)
            step += 1
            if step == k: 
                res = root.val
                return 

            if res is None: 
                dfs(root.right)
            
        
        dfs(root)
        return res

 

        
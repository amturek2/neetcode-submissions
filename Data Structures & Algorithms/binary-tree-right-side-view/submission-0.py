# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # always the root 
        # if there is a right side, we grab that on the level 
        # okay so basically the rightmost value on each level 

        res = []
        # for each level track the last seen 

        def bfs(node):
            if not node: 
                return 
            q = deque()
            q.append(node)

            while q: 
                level_size = len(q)
               

                for i in range(len(q)):
                    curr = q.popleft() 

                    if i == level_size - 1:
                        res.append(curr.val)
                    
    
                    if curr.left: 
                        q.append(curr.left)
                        
                    if curr.right: 
                        q.append(curr.right)

        bfs(root)

        return res


        
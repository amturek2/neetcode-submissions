class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True

            # 1. Check if current node violates its allowed range
            if not (min_val < node.val < max_val):
                return False

            # 2. Recurse left and right, ensuring both subtrees return True
            left_valid = dfs(node.left, min_val, node.val)
            right_valid = dfs(node.right, node.val, max_val)

            return left_valid and right_valid

        return dfs(root, float('-inf'), float('inf'))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longlen = 0
        
        def dfs(root):
            nonlocal longlen
            if not root:
                return 0

            if not root.left and not root.right:
                return 1
            
            leftheight = dfs(root.left)
            rightheight = dfs(root.right)
            curlen = leftheight + rightheight

            if curlen > longlen:
                longlen = curlen
            
            return max(leftheight, rightheight) + 1
        
        dfs(root)
        return longlen








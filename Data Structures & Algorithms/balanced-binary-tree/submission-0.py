# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True
        def nodeHeight(root: Optional[TreeNode]) -> int:
            nonlocal bal
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            lh = nodeHeight(root.left)
            rh = nodeHeight(root.right)
            height = abs(lh - rh)
            if height > 1:
                bal = False
            
            return max(lh, rh) + 1

        nodeHeight(root)
        
        return bal
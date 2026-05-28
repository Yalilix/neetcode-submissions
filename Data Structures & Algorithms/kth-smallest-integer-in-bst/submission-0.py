# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count(root) -> int:
            if root is None:
                return 0

            return 1 + count(root.left) + count(root.right)
        
        left_count = count(root.left) if root.left else 0
        if k <= left_count:
            return self.kthSmallest(root.left, k)
        print(root)
        if left_count + 1 == k:
            return root.val

        return self.kthSmallest(root.right, k - (left_count + 1))
        
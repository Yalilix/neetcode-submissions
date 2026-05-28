# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        ret = []

        while q:
            n = len(q)
            rightNode = None
            for i in range(n):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)

            if rightNode:
                ret.append(rightNode.val)
        return ret

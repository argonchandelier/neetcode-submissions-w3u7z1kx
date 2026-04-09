# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deeper(self, root, depth):
        ld = depth
        rd = depth
        if root.left:
            ld, bal = self.deeper(root.left, depth+1)
            if not bal:
                return 0, False
        if root.right:
            rd, bal = self.deeper(root.right, depth+1)
            if not bal:
                return 0, False
        maxDepth = max(ld, rd)

        bal = True
        if ld > rd+1 or rd > ld+1:
            bal = False

        return maxDepth, bal

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        d, bal = self.deeper(root, 1)

        return bal
        
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
            ld = self.deeper(root.left, depth+1)
        if root.right:
            rd = self.deeper(root.right, depth+1)
        
        return max(ld, rd)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        if root:
            return self.deeper(root, 1)
        else:
            return 0
        
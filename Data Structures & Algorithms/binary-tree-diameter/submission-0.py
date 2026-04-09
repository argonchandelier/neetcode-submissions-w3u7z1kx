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
        d1 = 0
        d2 = 0
        if root.left:
            ld, d1 = self.deeper(root.left, depth+1)
        if root.right:
            rd, d2 = self.deeper(root.right, depth+1)
        maxDepth = max(ld,rd)
        d = ld + rd - depth*2
        
        print(root.val, ld, rd, d, d1, d2)
        return maxDepth, max(d, d1, d2)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDepth, maxDist = self.deeper(root, 1)

        return maxDist
        
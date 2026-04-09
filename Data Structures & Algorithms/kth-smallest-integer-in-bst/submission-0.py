# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deeper(self, root):
        if not root:
            return
        
        self.deeper(root.left)
        self.i += 1
        if self.i >= self.k:
            if self.i == self.k:
                self.ans = root.val
            return
        self.deeper(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.k = k
        self.ans = -1

        self.deeper(root)

        return self.ans
        
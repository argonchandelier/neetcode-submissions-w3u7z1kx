# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deeper(self, rootp, rootq):
        if rootp.left is not None:
            if rootq.left is None or rootp.left.val != rootq.left.val:
                return False
        elif rootq.left is not None:
            return False

        if rootp.right is not None:
            if rootq.right is None or rootp.right.val != rootq.right.val:
                return False
        elif rootq.right is not None:
            return False
        
        if rootp.left:
            same = self.deeper(rootp.left, rootq.left)
            if not same:
                return False
        if rootp.right:
            same = self.deeper(rootp.right, rootq.right)
            if not same:
                return False
            
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q):
            return True
        elif p and q and p.val == q.val:
            same = self.deeper(p, q)
            return same
        return False
        
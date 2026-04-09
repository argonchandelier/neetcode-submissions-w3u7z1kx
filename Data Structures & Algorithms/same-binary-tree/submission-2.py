# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deeper(self, rootp, rootq, depth):
        if rootp.left is not None:
            if rootq.left is None or rootp.left.val != rootq.left.val:
                return None, False
        elif rootq.left is not None:
            return None, False
        if rootp.right is not None:
            if rootq.right is None or rootp.right.val != rootq.right.val:
                return None, False
        elif rootq.right is not None:
            return None, False
        
        dl = depth
        dr = depth
        if rootp.left:
            dl, same = self.deeper(rootp.left, rootq.left, depth+1)
            if not same:
                return None, False
        if rootp.right:
            dr, same = self.deeper(rootp.right, rootq.right, depth+1)
            if not same:
                return None, False
            
        return max(dl, dr), True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q):
            return True
        elif p and q and p.val == q.val:
            d, same = self.deeper(p, q, 1)
            return same
        return False
        
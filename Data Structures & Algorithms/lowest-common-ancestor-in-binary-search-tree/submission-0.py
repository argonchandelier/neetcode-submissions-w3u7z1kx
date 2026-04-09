# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deeper(self, root):
        if not root:
            return False, False
        
        pal, qal = self.deeper(root.left)
        if pal and qal:
            return True, True
        par, qar = self.deeper(root.right)
        if par and qar:
            return True, True
        pat, qat = root.val == self.p, root.val == self.q

        pa = pal or par or pat
        qa = qal or qar or qat

        if pa and qa:
            self.lca = root
            return True, True
        
        return pa, qa

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p = p.val
        self.q = q.val
        self.lca = None

        self.deeper(root)

        return self.lca
        
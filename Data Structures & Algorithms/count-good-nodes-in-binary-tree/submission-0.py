# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deeper(self, root, prevMax):
        if not root:
            return
        
        if root.val >= prevMax:
            prevMax = root.val
            self.good += 1
        
        self.deeper(root.left, prevMax)
        self.deeper(root.right, prevMax)

    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        self.deeper(root, root.val)

        return self.good

        
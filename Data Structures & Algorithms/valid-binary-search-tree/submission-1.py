# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # root.val still has to be bigger than anything to the left of its root, etc., same with right
    def deeper(self, root, minPrev, maxPrev, left):
        if not root:
            return True
        
        #print(left, minPrev, maxPrev, root.val)
        #if (left and root.val >= minPrev) or ((not left) and root.val <= maxPrev):
            #print("invalid")
            #return False
        if not (minPrev < root.val < maxPrev):
            return False
        '''
        if left:
            minPrev = root.val
        else:
            maxPrev = root.val
        '''

        valid = self.deeper(root.left, minPrev, root.val, True)
        if valid:
            valid = self.deeper(root.right, root.val, maxPrev, False)
        return valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.deeper(root.left, float('-inf'), root.val, True) and self.deeper(root.right, root.val, float('inf'), False)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = [root]
        dq = [0]
        prevd = 0
        lastVal = -1
        ans = []
        while q:
            cur = q.pop(0)
            d = dq.pop(0)

            if d > prevd:
                ans.append(lastVal)
            
            if cur.left:
                q.append(cur.left)
                dq.append(d+1)
            if cur.right:
                q.append(cur.right)
                dq.append(d+1)
            
            lastVal = cur.val
            prevd = d
        
        ans.append(lastVal)
        return ans

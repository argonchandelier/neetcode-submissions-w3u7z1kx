# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        dq = [0]
        depth = 0
        ans = [[]]
        while q:
            cur = q.pop(0)
            d = dq.pop(0)

            if d > depth:
                depth += 1
                ans.append([cur.val])
            else:
                ans[-1].append(cur.val)

            if cur.left:
                q.append(cur.left)
                dq.append(d+1)
            if cur.right:
                q.append(cur.right)
                dq.append(d+1)
        
        return ans

        
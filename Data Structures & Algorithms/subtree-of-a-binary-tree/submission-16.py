# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # before was ineff because we would check same things twice in comparing and not comparing modes, which gets exponential
    def deeper(self, root):
        if not root:
            return False
        
        if root.val == self.subrootTop.val:
            found = self.deeperCompare(root, self.subrootTop)
            if found:
                return True
        
        found = self.deeper(root.left)
        if not found:
            found = self.deeper(root.right)
            if not found:
                return False
        return True
    
    def deeperCompare(self, root, subroot):
        if not root:
            if subroot:
                return False
            else:
                return True
        elif not subroot:
            return False
        
        if root.val != subroot.val:
            return False
        
        same = self.deeperCompare(root.left, subroot.left)
        if same:
            same = self.deeperCompare(root.right, subroot.right)
            if same:
                return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #print("")
        if not subRoot:
            return True
        elif root:
            self.subrootTop = subRoot
            return self.deeper(root)
        return False

'''
class Solution:
    # Why does this stupid chatgpt code work, and mine doesn't?
    def isMatch(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return (
            root.val == subRoot.val and
            self.isMatch(root.left, subRoot.left) and
            self.isMatch(root.right, subRoot.right)
        )

    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False

        # Check if the current subtree matches
        if self.isMatch(root, subRoot):
            return True

        # Otherwise, check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
'''
'''
import sys

class Solution:
    # Start over because tree from original root is allowed to have duplicate values
    def deeper(self, root, subroot, comparingSubroot): # if comparingSubRoot is None, we aren't comparing
        # Even if we are comparing, we want to look at if subroot.val might match root's l/r/self val again
        # We have to look at all of root's vals, and even split off each time subroot start val is same
        # When resurfacing to subroot's top val, only then can we say the whole subroot has been found within
        # In the split off, we can still surface up to the split off point if a comparison is bad immediately
        #print(root.val, comparingSubroot.val if comparingSubroot else None)
        #print("")
        found = False
        if root.val == subroot.val:
            #print("subroot match start", subroot.val)
            sys.stdout.flush()
            samel = False
            samer = False
            if root.left and subroot.left:
                samel, found = self.deeper(root.left, subroot, subroot.left)
                if found:
                    return True, True
            elif (not root.left) and (not subroot.left):
                samel = True

            if samel:
                if root.right and subroot.right:
                    samer, found = self.deeper(root.right, subroot, subroot.right)
                    if found:
                        return True, True
                elif (not root.right) and (not subroot.right):
                    samer = True
            
                if samer: # found!
                    return True, True
            
        if comparingSubroot:
            if (root.val != comparingSubroot.val) or (root.left and not comparingSubroot.left) or (not root.left and comparingSubroot.left) or (root.right and not comparingSubroot.right) or (not root.right and comparingSubroot.right):
                comparingSubroot = None

        samel, samer = False, False
        if root.left:
            samel, found = self.deeper(root.left, subroot, comparingSubroot.left if comparingSubroot else None)
            if found:
                return True, True
        elif comparingSubroot and not comparingSubroot.left:
            samel = True
        if root.right:
            samer, found = self.deeper(root.right, subroot, comparingSubroot.right if comparingSubroot else None)
            if found:
                return True, True
        elif comparingSubroot and not comparingSubroot.right:
            samer = True
        
        if samel and samer:
            return True, False
        return False, False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print("")
        if not subRoot:
            return True
        elif root:
            same, found = self.deeper(root, subRoot, subRoot if root.val == subRoot.val else None)
            return found
        return False
'''
        
'''
    def deeper(self, root, subroot, comparing, d):
        print(root.val if root else None, subroot.val if subroot else None, comparing, d)
        found = False
        if comparing:
            found = True 
            if root.val != subroot.val:
                return [False]
        
        if root.left:
            if comparing and not subroot.left:
                return [False]
            same = self.deeper(root.left, subroot.left if comparing else subroot, comparing or subroot.val==root.left.val, d+1)
            if not same[0]:
                return [False]
            elif same[1]:
                found = True
        elif subroot.left and comparing:
            return [False]
        if root.right:
            if comparing and not subroot.right:
                return [False]
            same = self.deeper(root.right, subroot.right if comparing else subroot, comparing or subroot.val==root.right.val, d+1)
            if not same[0]:
                return [False]
            elif same[1]:
                found = True
        elif subroot.right and comparing:
            return [False]
        
        return [True, found, d]

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if root:
            same = self.deeper(root, subRoot, root.val==subRoot.val, 1)
            if same[0]:
                print("H", same[1])
                return same[1]
        return False
    '''
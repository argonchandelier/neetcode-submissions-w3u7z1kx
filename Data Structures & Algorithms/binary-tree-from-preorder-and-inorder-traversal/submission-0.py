# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 1. go down po until io match, which means no more to the left
    # 2. if next io not already in po, then repeat 1 (on newNode is right node), else go to 3
    # 3. move back a node
    def buildSubNodes(self, node):
        #print(self.po, self.io, node.val)
        if node.val != self.io[0]: # start of step 1, going down po
            valL = self.po.pop(0)
            self.seen[valL] = 1
            nodeL = TreeNode(valL)
            node.left = nodeL
            self.buildSubNodes(nodeL)
            #print(valL, "l done")
        
        #print("pop io", self.io[0])
        self.io.pop(0) # center, root node, which is this nodes's val

        if self.io and self.io[0] not in self.seen: # there is something to the right
            valR = self.po.pop(0)
            self.seen[valR] = 1
            nodeR = TreeNode(valR)
            node.right = nodeR
            self.buildSubNodes(nodeR)
        #if self.io[0] == self.po[0]
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.po = preorder
        self.io = inorder
        self.seen = {self.po[0]: 1}

        node = TreeNode(self.po.pop(0))
        self.buildSubNodes(node)
        print(self.po, self.io, self.seen)

        return node

    '''
    def buildSubNodes(self, node):
        if node.val == self.io[0]:
            self.seen[self.io.pop(0)] = 1
            #self.po.pop(0)
            if self.po[0] == self.io[0]:
                # right branch?
                newNode2 = TreeNode(self.po.pop(0))
                node.right = newNode2
                self.buildSubNodes(newNode2)
        else:
            newNode = TreeNode(self.po.pop(0))
            node.left = newNode
            self.buildSubNodes(newNode)
            self.io.pop(0) # should be node.val???
            if self.po[0] == self.io[0]:
                # right branch
                newNode2 = TreeNode(self.po.pop(0))
                node.right = newNode2
                self.buildSubNodes(newNode2)
    '''
    
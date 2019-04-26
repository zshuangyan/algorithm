class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNode(self, root):
        if not root:
            return 0
        
        return self.sumNode(root.left) + root.val + self.sumNode(root.right)
        
    def rangeSumL(self, root, L):
        if root.val == L:
            return root.val + self.sumNode(root.right)
        
        elif root.val < L:
            return self.rangeSumL(root.right, L)
        
        else:
            return self.rangeSumL(root.left, L) + root.val + self.sumNode(root.right)
        
    def rangeSumR(self, root, R):
        if root.val == R:
            return root.val + self.sumNode(root.left)
        
        elif root.val > R:
            return self.rangeSumR(root.left, R)
            
        else:
            return self.rangeSumR(root.right, R) + root.val + self.sumNode(root.left)

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root.val == L:
            return root.val + self.rangeSumR(root.right, R)
        
        elif root.val == R:
            return root.val + self.rangeSumL(root.left, L)
        
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        
        else:
            return self.rangeSumL(root.left, L) + root.val + self.rangeSumR(root.right, R)

from binary_search_tree import Node, BSTree

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not tin:
            return None
        root_val = pre[0]
        root_pos = tin.index(root_val)
        left_num = root_pos
        left = self.reConstructBinaryTree(pre[1: 1+left_num], tin[:root_pos])
        right = self.reConstructBinaryTree(pre[1+left_num:], tin[root_pos+1:])
        root = Node(root_val)
        root.left = left
        root.right = right
        assert bst.inOrder(root) == tin
        assert bst.preOrder(root) == pre
        return root


bst = BSTree()
a = [1,3,9,4,7,2,8,6]
import random
random.shuffle(a)
for num in a:
    bst.insert(num)
bst.printTree()
t = bst.inOrder(bst.root)
p = bst.preOrder(bst.root)

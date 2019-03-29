class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        stack = []
        cur = root
        result = []
        while len(stack) != 0 or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if len(result) > 0 and result[-1] >= cur.val:
                return False
            result.append(cur.val)
            cur = cur.right
            
        return True

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

input = ["10", "5", "15", "null", "null", "6", "20"]
def stringToTreeNode(input):
    if not input:
        return None

    inputValues = [s.strip() for s in input]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def print_tree(root):
    print(root.val)
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)


root = stringToTreeNode(input)
print_tree(root)
result = Solution().isValidBST(root)
print(result)

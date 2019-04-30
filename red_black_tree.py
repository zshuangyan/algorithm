class TreeNode:
    def __init__(self, x):
        self.val = x
        self.count = 1
        self.left = None
        self.right = None
        self.color = 1 # 1 for red and 0 for black
        
class RBTree:
    def __init__(self):
        self.root = None

    def heightNode(self, node):
        if not node:
            return 0

        left_height = self.heightNode(node.left)
        right_height = self.heightNode(node.right)
        max_height = max(left_height, right_height)
        return max_height + 1
    
    def width(self, height):
        return pow(2, height) - 1
    
    def get_child_pos(self, pos, child_height):
        grand_child_width = self.width(child_height-1)
        return pos - (grand_child_width+1), pos + (grand_child_width+1)
        
            
    def print_tree_matrix(self):
        if not self.root:
            return [[]]

        height = self.heightNode(self.root)
        width = self.width(height)
        matrix = [[" " for i in range(width)] for j in range(height)]
        root_pos = width // 2
        stack = [(self.root, root_pos)]
        for i in range(height):
            for j in range(2**i):
                node, node_pos = stack.pop(0)
                if node:
                    matrix[i][node_pos] = str(node.val)
                if i == height -1:
                    continue
                    
                left_pos, right_pos = self.get_child_pos(node_pos, height-i-1)
                if node:
                    node_left = node.left
                    node_right = node.right
                else:
                    node_left = None
                    node_right = None
                    
                stack.append((node_left, left_pos))
                stack.append((node_right, right_pos))
        return matrix

    def printTree(self):
        if not self.root:
            print("Empty tree")
            return

        matrix = self.print_tree_matrix()
        for row in matrix:
            print("".join(row))


        matrix = self.print_tree_matrix()
        
    def flipColor(self, color):
        return 1 - color
        
    def flipNodeColor(self, node):
        node.color = self.flipColor(node.color)
        node.left.color = self.flipColor(node.left.color)
        node.right.color = self.flipColor(node.right.color)
        
    def rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = 1
        return x
        
    def rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = 1
        return x
        
    def isRed(self, node):
        if not node:
            return False
        
        return node.color == 1
        
    def insertNode(self, node, value):
        if not node:
            node = TreeNode(value)
            return node
        
        elif node.val == value:
            node.count += 1
            return node
        
        elif node.val > value:
            node.left = self.insertNode(node.left, value)
            
        else:
            node.right = self.insertNode(node.right, value)
            
        if self.isRed(node.right):
            node = self.rotateLeft(node)
            
        if self.isRed(node.left) and self.isRed(node.left.right):
            node.left = self.rotateLeft(node.left)
            
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
            
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipNodeColor(node)
            
        return node
            
            
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.root = self.insertNode(self.root, value)
        self.root.color = 0

if __name__ == "__main__":
    rbt = RBTree()
    for num in [1,3,6,9,2,7,5,4,8,3,2,8,4]:
        rbt.insert(num)
    rbt.printTree() 

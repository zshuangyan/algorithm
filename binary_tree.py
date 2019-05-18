class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        
    def inOrder(self, node):
        if not node:
            return []
            
        stack = [node]
        tmp = []
        result = []
        while stack:
            node = stack.pop()
            while node:
                tmp.append(node)
                node = node.left
            
            while tmp:
                node = tmp.pop()
                result.append(node.val)
                if node.right:
                   stack.append(node.right)
                   break
                   
        return result

    def preOrder(self, node):
        if not node:
            return []

        stack = [node]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


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

class Node:
    def __init__(self, start, end, value, left=None, right=None):
        self.start = start
        self.end = end
        self.value = value
        self.left = left
        self.right = right

class FragmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.index = self.buildIndex(0, len(nums)-1)

    def buildIndex(self, start, end):
        if start == end:
            return Node(start, end, self.nums[start])

        node = Node(start, end, 0)
        mid = (start + end) // 2
        node.left = self.buildIndex(start, mid)
        node.right = self.buildIndex(mid+1, end)
        node.value = max(node.left.value, node.right.value)
        return node
    
    def update(self, pos, value):
        self.nums[pos] = value
        self.updateNode(self.index, pos, value)
        
    def updateNode(self, node, pos, value):
        if not node:
            return 
        
        if pos < node.start or pos > node.end:
            return
        
        if node.start == node.end == pos:
            node.value = value
            return
        
        max_value = None
        if node.left:
            self.updateNode(node.left, pos, value)
            max_value = node.left.value
            
        if node.right:
            self.updateNode(node.right, pos, value)
            max_value = max(node.right, max_value)
            
        node.value = max_value
        return
            
            

    def searchNode(self, node, start, end):
        if node.end < start or node.start > end:
            raise Exception("node contain no item in [%s, %s]" % (start, end))

        if start <= node.start and node.end <= end:
            return node.value

        max_value = None
        try:
            left_value = self.searchNode(node.left, start, end)
        except Exception:
            pass
        else:
            max_value = left_value

        try:
            right_value = self.searchNode(node.right, start, end)
        except Exception:
            pass
        else:
            if not max_value or max_value < right_value:
                max_value = right_value

        return max_value

    def search(self, start, end):
        return self.searchNode(self.index, start, end) 

assert 8 == FragmentTree([3, 8, 1, 6]).search(0,3)
assert 6 == FragmentTree([3, 8, 1, 6]).search(2,3)
assert 8 == FragmentTree([3, 8, 1, 6]).search(1, 2)
f = FragmentTree([3, 8, 1, 6])
f.update(1, 7)
assert 7 == f.search(1,2)

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
        if not nums:
            return
        self.index = self.buildIndex(0, len(nums)-1)
        
    def printNode(self, node):
        if not node:
            return 
        
        print(node.value)
        self.printNode(node.left)
        self.printNode(node.right)
        

    def buildIndex(self, start, end):
        if start == end:
            return Node(start, end, self.nums[start])

        node = Node(start, end, 0)
        mid = (start + end) // 2
        node.left = self.buildIndex(start, mid)
        node.right = self.buildIndex(mid+1, end)
        node.value = node.left.value + node.right.value
        return node
    
    def update(self, pos, value):
        difference = value - self.nums[pos]
        self.nums[pos] = value
        self.updateNode(self.index, pos, difference)
        
    def updateNode(self, node, pos, difference):
        if not node:
            return 
        
        if pos < node.start or pos > node.end:
            return
        
        node.value += difference
        if node.start == node.end == pos:
            return
        self.updateNode(node.left, pos, difference)
        self.updateNode(node.right, pos, difference)
            

    def sumRangeNode(self, node, start, end):
        import pdb;pdb.set_trace()
        if node.end < start or node.start > end:
            raise Exception("node contain no item in [%s, %s]" % (start, end))

        if start <= node.start and node.end <= end:
            return node.value

        sum = 0
        try:
            left_value = self.searchNode(node.left, start, end)
        except Exception:
            pass
        else:
            sum += left_value

        try:
            right_value = self.searchNode(node.right, start, end)
        except Exception:
            pass
        else:
            sum += right_value

        return sum

    def sumRange(self, start, end):
        return self.sumRangeNode(self.index, start, end)

result = FragmentTree([3, -8]).sumRange(1,1)
print(result)

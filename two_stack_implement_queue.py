class StackFullError(Exception):
    pass

class Stack:
    def __init__(self):
        self.data = []
        self.length = 0
        
    def push(self, value):
        self.data.append(value)
        self.length += 1
        
        
    def pop(self):
        self.length -= 1
        return self.data.pop()
        
    def empty(self):
        return self.length == 0
        
class Solution:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    def push(self, node):
        # write code here
        self.s1.push(node)
        
    def pop(self):
        # return xx
        if self.s2.empty():
            while self.s1.length:
                self.s2.push(self.s1.pop())
        return self.s2.pop()

s = Solution()
s.push(1)
value = s.pop()
print(value)

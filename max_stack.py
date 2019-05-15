class StackFullError(Exception):
    pass
    
    
class StackEmptyError(Exception):
    pass


class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.len = 0
        self.data = []
        self.max = None
        
    
    def max_value(self):
        if self.len == 0:
            raise StackEmptyError("stack is empty")
            
        return self.max 
        
    def push(self, value):
        if self.len == self.cap:
            raise StackFullError("stack is full")
        elif self.len == 1:
            self.data.append(value)
            self.max = value
        elif value > self.max:
            t = 2*value - self.max
            self.data.append(t)
            self.max = value
        else:
            self.data.append(value)
        self.len += 1
        
    def pop(self):
        if self.len == 0:
           raise StackEmptyError("stack is empty")
        self.len -= 1
        top_value = self.data.pop()
        if top_value <= self.max:
            return top_value
        else:
            max_value = self.max
            self.max = 2*self.max - top_value
            return max_value
            
            
s = Stack(3)
for i in [1,3,4]:
    s.push(i)
    print("push: %s to stack, max value in stack: %s" % (i, s.max_value()))
for i in range(2):
    value = s.pop()
    print("value popped: %s, max value in stack: %s" % (value, s.max_value()))
    
            
            
        
        




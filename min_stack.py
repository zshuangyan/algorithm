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
            
        top_value = self.data[self.len - 1]
             
        
        
    def push(self, value):
        if self.len == self.cap:
            raise StackFullError("stack is full")
        if value > self.max:
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
            
            
        return self.data.pop()
        
        




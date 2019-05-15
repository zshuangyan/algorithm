class HeapEmptyError(Exception):
    pass

class Heap:
    def __init__(self):
        # 设置占位符方便计算
        self.data = [""]
        self.len = 1

    def compare(self, v1, v2):
        pass


    def push(self, value):
        self.data.append(value)
        self.len += 1
        pos = self.len - 1
        tmp = self.data[pos]
        while True:
            if pos <= 1:
                break
            parent_pos = pos // 2
            if self.compare(self.data[parent_pos], tmp):
                break
            self.data[pos] = self.data[parent_pos]
            pos = parent_pos
        self.data[pos] = tmp
        

    def pop(self):
        if self.len == 1:
            raise HeapEmptyError("heap is empty")
        pos = 1
        pop_value = self.data[pos]
        r_value = self.data.pop()
        self.len -= 1
        while True:
            left, right = 2 * pos, 2 * pos + 1
            if left > self.len - 1:
                break
            elif right > self.len -1:
                child_pos = left
            elif self.compare(self.data[left], self.data[right]):
                child_pos = left
            else:
                child_pos = right

            if self.compare(r_value, self.data[child_pos]):
                break
            self.data[pos] = self.data[child_pos]
            pos = child_pos
        if self.len > 1:
            self.data[pos] = r_value
        return pop_value
    
    
class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def compare(self, v1, v2):
        return v1 < v2


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = MinHeap()
        for head in lists:
            while head:
                h.push(head.val)
                head = head.next
        
        try:
            value = h.pop()
        except HeapEmptyError:
            return None
        
        current = head = ListNode(value)
        while True:
            try:
                value = h.pop()
                current.next = ListNode(value)
                current = current.next
            except HeapEmptyError:
                break
                
        return head

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

class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def compare(self, v1, v2):
        return v1 > v2

class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def compare(self, v1, v2):
        return v1 < v2

if __name__ == "__main__":
    import random
    
    print("testing MinHeap")
    for i in range(3):
        h = MinHeap()
        input_num = random.sample([i for i in range(1,10)], 6)
        for i in input_num:
            h.push(i)
        result = []
        for i in range(6):
            result.append(h.pop())
        print("input: %s" % input_num)
        print("result: %s" % result)
        print()
        assert result == sorted(input_num)

    print("testing MaxHeap")
    for i in range(3):
        h = MaxHeap()
        input_num = random.sample([i for i in range(1,10)], 6)
        for i in input_num:
            h.push(i)
        result = []
        for i in range(6):
            result.append(h.pop())
        print("input: %s" % input_num)
        print("result: %s" % result)
        print()
        assert result == sorted(input_num, reverse=True)


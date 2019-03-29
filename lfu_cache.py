class Node:
    def __init__(self, key, value, count=1):
        self.key = key
        self.value = value
        self.count = count
        self.prev = None
        self.next = None

    def __str__(self):
        return "%s: %s, count: %s" % (self.key, self.value, self.count)
        
class DLinkedList:
    def __init__(self):
        self.head = Node(-1, -1, 0)
        self.tail = Node(-1, -1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        output = ""
        cur = self.head
        while cur != self.tail:
            output += str(cur) + "\n"
            cur = cur.next
        output += str(cur)
        return output
        
        
    def append(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node
    
    def remove_last(self):
        node = self.tail.prev
        self.remove(node)
        return node
    
    def empty(self):
        return self.head.next == self.tail
        
class LFUCache:
            
    def __init__(self, capacity: int):
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.tree = dict()
        
    def _insert(self, node, count):
        if self.tree.get(count) is None:
            self.tree[count] = DLinkedList()
        self.tree[count].append(node)
            
    def _remove(self):
        smallest = min(key for key in self.tree)
        node = self.tree[smallest].remove_last()
        if self.tree[smallest].empty():
            del self.tree[smallest]
        return node

    def get(self, key: int) -> int:
        if self.cache.get(key):
            node = self.cache.get(key)
            self.tree[node.count].remove(node)
            if self.tree[node.count].empty():
                del self.tree[node.count]
            node.count += 1
            self._insert(node, node.count)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        if self.cache.get(key) is not None:
            node = self.cache.get(key)
            self.tree[node.count].remove(node)
            if self.tree[node.count].empty():
                del self.tree[node.count]
            node.count += 1
            node.value = value
            self._insert(node, node.count)
            return
        node = Node(key, value)
        if self.size < self.capacity:   
            self._insert(node, 1)
            self.cache[key] = node
            self.size += 1
        else:
            remove_node = self._remove()
            del self.cache[remove_node.key]
            self._insert(node, 1)
            self.cache[key] = node

def print_tree(tree):
    for key, dl in tree.items():
        print("count: %s" % key)
        print("double_list:\n%s" % dl)
    print()

inputs = ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
params = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
lfu = LFUCache(params[0][0])
for method, inner_params in zip(inputs[1:], params[1:]):
    if method == "put":
        print("put %s: %s" % (inner_params[0], inner_params[1]))
        lfu.put(*inner_params)
        print_tree(lfu.tree)
    else:
        result = lfu.get(*inner_params)
        print("get %s: %s" % (inner_params[0], result))
        print_tree(lfu.tree)
    print()


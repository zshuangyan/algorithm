class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return pHead
        
        pPrev = None
        pCurrent = pHead
        while pCurrent:
            tmp = pCurrent.next
            pCurrent.next = pPrev
            pPrev = pCurrent
            pCurrent = tmp
            
        return pPrev

current = head = ListNode(1)
for i in range(2,6):
    node = ListNode(i)
    current.next = node
    current = node

def print_list(head):
    node = head
    while node:
        print("node: %s" % node.val)
        node = node.next

print_list(head)
print()
r_head = Solution().ReverseList(head)
print_list(r_head)
	

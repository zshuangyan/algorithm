class Solution:
    def insertHeap(self, h, num):
        h.append(num)
        pos = len(h) - 1
        while pos > 1 and h[pos//2] < num:
                h[pos] = h[pos//2]
                pos = pos//2
        h[pos] = num
        
    def deleteHeap(self, h):
        value = h.pop()
        if len(h) == 1:
            return
        pos = 1
        while 2*pos <= len(h)-1 and h[pos] > value:
            if 2*pos == len(h)-1 or h[pos*2] > h[pos*2+1]:
                if h[pos*2] <= value:
                    break
                h[pos] = h[pos*2]
                pos = pos*2
            else:
                if h[pos*2+1] <= value:
                    break
                h[pos] = h[pos*2+1]
                pos = pos*2 + 1
        h[pos] = value
            
    def findKthLargest(self, nums: list, k: int) -> int:
        heap = [0]
        for num in nums:
            self.insertHeap(heap, num)
        for i in range(k-1):
            self.deleteHeap(heap)
        return heap[1]


result = Solution().findKthLargest([10,6,9,5,4,7,8], 2)
print(result)
result = Solution().findKthLargest([-1, 2, 0], 2)
print(result)

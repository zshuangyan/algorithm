import random
class Solution:
    def min_index(self, heights, start, end):
        if start == end:
            return start
        min_value = heights[start]
        index = start
        for i in range(start+1, end+1):
            if heights[i] < min_value:
                min_value = heights[i]
                index = i
        return index
    
    def subLargest(self, heights, start, end):
        if start > end:
            return 0
        if start == end:
            return heights[start]
        min_index = self.min_index(heights, start, end)
        split_index = random.randint(start, end)
        left = self.subLargest(heights, start, split_index)
        right = self.subLargest(heights, split_index, end)
        contain_min = heights[min_index] * (end-start+1)
        return max([left, right, contain_min])
    
    def largestRectangleArea(self, heights: list) -> int:
        if not heights:
            return 0
        
        import pdb;pdb.set_trace()
        return self.subLargest(heights, 0, len(heights) - 1)

Solution().largestRectangleArea([2,1,5,6,2,3])

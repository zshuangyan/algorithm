class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        results = []
        index = len(nums) - 1
        while index >= 0:
            num = nums[index]
            index -= 1
            max_length = 0
            new_item = None
            to_remove = -1
            for i, item in enumerate(results):
                if num < item[0] and len(item) > max_length:
                    new_item = [num] +  item
                    max_length = len(item)
                    if num == item[0] - 1:
                        to_remove = i
            if to_remove != -1:
                results.pop(to_remove)
            if new_item is None:
                new_item = [num]
            results.append(new_item)
        length = max([len(result) for result in results])
        return length

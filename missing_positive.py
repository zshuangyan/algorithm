class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        if not nums:
            return 1
        
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1
            
        nums = [num for num in nums if num > 0]
        print(nums)
        
        for i in range(len(nums)):
            pos = i
            # find i-th smallest value position
            for j in range(i+1, len(nums)):
                if nums[j] < nums[pos]:
                    pos = j
                    
            # swap nums[i] with nums[pos]
            tmp_value = nums[i]
            nums[i] = nums[pos]
            nums[pos] = tmp_value
            
            # handle history
            if i == 0:
                if nums[i] > 1:
                    return 1
            else:
                print("i: %s, nums: %s" % (i, nums))
                if nums[i] > nums[i-1] + 1:
                    return nums[i-1] + 1
            print("i: %s, nums: %s" % (i, nums))
                
        return nums[-1] + 1

result = Solution().firstMissingPositive([1, 1001])
print(result)

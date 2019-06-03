class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        while True:
            value = rotateArray.pop(0)
            if value <= rotateArray[0] and value < rotateArray[-1]:
                return value
            else:
                rotateArray.append(value)

s = Solution()
result = s.minNumberInRotateArray([3,4,5,1,2])
print(result)
result = s.minNumberInRotateArray([1,2,3,4,5])
print(result)
result = s.minNumberInRotateArray([5,4,3,2,1])
print(result)

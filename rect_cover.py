class Solution:
    def zuhe(self, num, choice):
        value = num - choice
        value = min(choice, num-choice)
        fenzi, fenmu = 1, 1
        for i in range(choice):
            fenzi *= (num - i)
            fenmu *= (choice - i)
        return fenzi // fenmu
    
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        x = number // 2
        total_num = 0
        for i in range(x+1):
            positions = i + number - 2*i
            total_num +=  self.zuhe(positions, i)
        return total_num

s = Solution()
result = s.rectCover(3)
print(result)
result = s.rectCover(4)
print(result)
result = s.rectCover(5)
print(result)

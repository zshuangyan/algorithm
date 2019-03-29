import random
class Solution:
    def canJump(self, nums: list) -> bool:
        if len(nums) <= 1:
            return True
        avails = set([0])
        last_index = len(nums) - 1
        loop = 0
        while True:
            print("loop: %s" % loop)
            loop += 1
            old_avails = set(avails)
            new_avails = set()
            print("old_avails", old_avails)
            for index in old_avails:
                step = nums[index]
                for i in range(step, 0, -1):
                    tmp_index = index + i
                    if tmp_index == last_index:
                        return True
                    if (tmp_index not in new_avails) and (tmp_index not in old_avails):
                        new_avails.add(tmp_index)
            print("new_avails", new_avails)
            print()
            if not new_avails:
                return False
            else:
                avails = new_avails


for i in range(8):
    poss = [0 for i in range(5)] + [ 1 for i in range(10)] + [2 for i in range(10)] + [3 for i in range(10)] + [4 for i in range(8)] + [5 for i in range(4)] + [6, 7, 8]
    input_nums = [random.choice(poss) for i in range(30)]
    print(input_nums, sep=" ")
    result = Solution().canJump(input_nums)
    print(result)

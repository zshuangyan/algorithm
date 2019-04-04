class Solution:                
    def findRadius(self, houses, heaters):
        def check(house, radius, start, end):
            least_distance = None
            stack = [(start, end)]
            while stack:
                start, end = stack.pop()
                if house <= heater_list[start]:
                    tmp_distance = heater_list[start] - house
                    if tmp_distance <= radius:
                        return radius
                    if not least_distance or least_distance > tmp_distance:
                        least_distance = tmp_distance
                elif house >= heater_list[end]:
                    tmp_distance = house - heater_list[end]
                    if tmp_distance <= radius:
                        return radius
                    if not least_distance or least_distance > tmp_distance:
                        least_distance = tmp_distance
                else:
                    mid = (start + end) // 2
                    stack.append((start, mid))
                    stack.append((mid+1, end))
            return least_distance

        house_set = set(houses)
        heater_set = set(heaters)
        heater_list = sorted(heater_set)
        upper = len(heater_list) - 1
        longest = 0
        for house in house_set:
            distance = check(house, longest, 0, upper)
            if distance > longest:
                longest = distance
        return longest

MAX = 25
import random
s = Solution()
for i in range(8):
   num_of_houses = random.randint(1,20)
   num_of_heaters = random.randint(1,8)
   houses = [random.randint(1,MAX) for i in range(num_of_houses)]
   heaters = [random.randint(1,MAX) for i in range(num_of_heaters)]
   result = s.findRadius(houses, heaters)
   print("houses: %s\nheaters: %s\nresult: %s" % (houses, heaters, result))

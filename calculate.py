import re
left_ass = ["-", "*", "/"]
seps = ["\+", "\-", "\(", "\)", "\*", "/"]
prefer = {"+": 1, "-": 1, "*": 2, "/": 2}
class Solution:
    def postfix(self, s):
        queue = []
        stack = []
        chars = [c.strip() for c in re.split("(%s)" % "|".join(seps), s) if c.strip()]
        for c in chars:
            if c == "(":
                stack.append(c)
            elif c in prefer:
                while stack:
                    if stack[-1] in prefer and \
                    ((prefer[stack[-1]] > prefer[c]) or (prefer[stack[-1]] == prefer[c] and stack[-1] in left_ass)):
                        tmp = stack.pop()
                        queue.append(tmp)
                    else:
                        break
                stack.append(c)
            elif c == ")":
                tmp = stack.pop()
                while tmp != "(":
                    queue.append(tmp)
                    tmp = stack.pop()
            else:
                queue.append(int(c))
        while stack:
            tmp = stack.pop()
            queue.append(tmp)
        return queue
    
    def calculate_post(self, queue):
        stack = []
        for item in queue:
            if item in prefer:
                right = stack.pop()
                left = stack.pop()
                if item == "+":
                    result = left + right
                elif item == "-":
                    result = left - right
                elif item == "*":
                    result = left * right
                else:
                    result = left // right
                stack.append(result)
            else:
                stack.append(item)
        return stack[0]
        
    def calculate(self, s: str) -> int:
        post = self.postfix(s)
        print(post)
        result = self.calculate_post(post)
        return result

result = Solution().calculate("1+2*5/3+6/4*2")
print(result)

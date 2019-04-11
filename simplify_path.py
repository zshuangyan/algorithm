class Solution:
    def simplifyPath(self, path: str) -> str:
        # handle path empty or only contain one character
        length = len(path)
        if length <= 1:
            return "/"

        parts = ["/"]
        index = 0
        stack = ""
        for index in range(length):
            # current character is "/"
            if path[index] == "/":
                if not stack:
                    continue
                else:
                    if stack == ".":
                        pass
                    elif stack == "..":
                        if len(parts) == 1:
                            pass
                        else:
                            parts = parts[:-1] 
                    else:
                        parts.append(stack)

                    stack = ""

            else:
                stack += path[index]
            #print("index: %s, path[index]: %s, parts: %s, stack: %s" % (index, path[index], parts, stack))

        if stack:
            if stack == "..":
                if len(parts) != 1:
                    parts = parts[:-1]
            elif stack != ".":
                parts.append(stack)
        
        return parts[0] + '/'.join(parts[1:])
                    
s = Solution()
for path in ["/", "/a/b", "/a/", "/a/..", "/a/./b", "/a/c./b", "/a/.c/b", "/a/../../.."]:
    result = s.simplifyPath(path)
    print("path: %s, simplified: %s" % (path, result))


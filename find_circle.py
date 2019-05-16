class Solution:
    def findCircle(self, numCourses: int, prerequisites: list) -> list:
        def dfs(node):
            if node in visited:
                return True
            
            if node in marked:
                nonlocal circle
                if not circle:
                    circle = [node]
                    current = prevNode[node]
                    while current != node:
                       circle.append(current)
                       current = prevNode[current]
                    circle.append(node)
                    print("circle: %s" % circle)
                    circle[:] = circle[::-1]
                return False
            else:
                marked.add(node)
                
            for nb in ad_list[node]:
                prevNode[nb] = node
                if not dfs(nb):
                    return False
            visited.add(node)
            marked.remove(node)
            return True
        
        ad_list = [[] for i in range(numCourses)]
        for node, prev in prerequisites:
            ad_list[prev].append(node)
            
        prevNode = [-1 for i in range(numCourses)]
        marked = set()
        visited = set()
        circle = []
        for i in range(numCourses):
            dfs(i)
        return circle

result = Solution().findCircle(2, [[0,1], [1,0]])
print(result)

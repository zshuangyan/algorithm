class Solution:
    def numIslands(self, grid: list) -> int:
        if not grid:
            return 0
        
        row, column = len(grid), len(grid[0])
        visited = [[0 for i in range(column)] for j in range(row)]
        count = 0
        for i in range(row):
            for j in range(column):
                if visited[i][j]:
                    continue
                    
                visited[i][j] = 1
                if grid[i][j] == '0':
                    continue
                    
                stack = [(i,j)]
                while stack:
                    pos_x, pos_y = stack.pop(0)
                    poss = [(pos_x-1, pos_y), (pos_x+1, pos_y), (pos_x, pos_y-1), (pos_x, pos_y+1)]
                    for x, y in poss:
                        if (not 0 <= x < row) or (not 0 <= y < column) or visited[x][y]:
                            continue

                        visited[x][y] = 1
                        if grid[x][y] == '1':
                            stack.append((x, y))
                count += 1
        return count

result = Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
assert result == 3

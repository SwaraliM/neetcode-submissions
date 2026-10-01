class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]
        maxArea = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            area = 1
            
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                
                    if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0):
                        continue
                    q.append((row,col))
                    grid[row][col] = 0
                    area += 1
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea




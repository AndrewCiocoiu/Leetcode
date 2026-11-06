from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        max_safeness = 0

        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1] == 1:
            return 0

        def BFS(thief_positions):
            nonlocal max_safeness

            q = deque(thief_positions)

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            curr_distance = 1
            while q:
                q_len = len(q)
                for i in range(q_len):
                    x, y = q.popleft()
                    for direction in directions:
                        nx = x + direction[0]
                        ny = y + direction[1]

                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == -1:
                            grid[nx][ny] = curr_distance
                            max_safeness = max(max_safeness, curr_distance)
                            q.append((nx, ny))
                
                curr_distance += 1
 
        def BFS2(starting_pos, safeness):

            if grid[starting_pos[0]][starting_pos[1]] < safeness:
                return False

            q = deque([starting_pos])

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited = set([starting_pos])


            while q:
                q_len = len(q)
                for i in range(q_len):
                    x, y = q.popleft()
                    if x == len(grid) - 1 and y == len(grid[0]) - 1:
                        return True
                    for direction in directions:
                        nx = x + direction[0]
                        ny = y + direction[1]

                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] >= safeness and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append((nx, ny))
                
            
            return False

        thief_positions = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j] = 0  
                    thief_positions.append((i, j))
                else:
                    grid[i][j] = -1


        BFS(thief_positions)

        left = 0
        right = max_safeness

        while(left <= right):
            mid = (left + right) // 2
            if (BFS2((0, 0), mid)):
                left = mid + 1
            else:
                right = mid - 1 

        return right
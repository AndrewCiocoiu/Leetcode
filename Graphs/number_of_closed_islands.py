class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def is_edge(x, y):
            return x == n - 1 or y == m - 1 or x == 0 or y == 0


        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def valid(i, j):
            is_valid = True

            if is_edge(i, j):
                is_valid = False

            grid[i][j] = 1

            q = deque([(i, j)])
        
            while q:
                curr_i, curr_j = q.popleft()
                for i_dir, j_dir in directions:
                    i_nbr, j_nbr = curr_i + i_dir, curr_j + j_dir

                    if 0 <= i_nbr < n and 0 <= j_nbr < m and grid[i_nbr][j_nbr] == 0:
                        if is_edge(i_nbr, j_nbr):
                            is_valid = False
                        
                        grid[i_nbr][j_nbr] = 1
                        q.append((i_nbr, j_nbr))
            
            return is_valid

        counter = 0
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 0 and valid(i, j)):
                    counter += 1

        return counter 
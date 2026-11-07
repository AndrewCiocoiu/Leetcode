class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        def can_swim(rising_water_level):
            visited = set([(0, 0)])
            q = deque([(0, 0)])
            n = len(grid)

            if grid[0][0] > rising_water_level:
                return False
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q:
                i, j = q.popleft()
                if i == n - 1 and j == n - 1:
                    return True
                
                for i_dir, j_dir in directions:
                    i_n, j_n = i + i_dir, j + j_dir

                    if 0 <= i_n <= n - 1 and 0 <= j_n <= n -1 and (i_n, j_n) not in visited and grid[i_n][j_n] <= rising_water_level:
                        visited.add((i_n, j_n))
                        q.append((i_n, j_n))
            
            return False
        
        max_rising_water = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_rising_water = max(max_rising_water, grid[i][j])
        
        left = 0
        right = max_rising_water

        while left < right:
            mid = left + (right - left) // 2
            if can_swim(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
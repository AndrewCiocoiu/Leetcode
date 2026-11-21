class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def calc_distance(x1, y1):
            return math.sqrt(math.pow(x1 - 0, 2) + math.pow(y1 - 0, 2))
        

        h = []

        for x, y in points:
            heapq.heappush(h, (calc_distance(x, y), x, y))
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(h)[1:])
        
        return res
from collections import defaultdict
from functools import cache
import sys

sys.setrecursionlimit(200000)

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj_list = defaultdict(list)
        bob_visit = defaultdict(lambda: float("inf"))

        print(bob_visit[0])

        for f, t in edges:
            adj_list[f].append(t)
            adj_list[t].append(f)

        def find_bob(node, parent, time):
            if node == 0:
                bob_visit[node] = time
                return True
            
            for neighbor in adj_list[node]:
                if neighbor != parent:
                    if find_bob(neighbor, node, time + 1):
                        bob_visit[node] = time
                        return True
            
            return False

        find_bob(bob, -1, 0)

        def DFS(val, i, parent, time):
            if time < bob_visit[i]:
                val += amount[i]
            elif time == bob_visit[i]:
                val += amount[i] // 2

            max_val = float("-inf")
            for children in adj_list[i]:
                if children != parent:
                    max_val = max(DFS(val, children, i, time + 1), max_val)

            return val if max_val == float("-inf") else max_val

        return DFS(0, 0, -1, 0)


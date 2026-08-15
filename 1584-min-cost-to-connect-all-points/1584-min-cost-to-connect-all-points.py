import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()

        min_heap = [(0, 0)]
        total_cost = 0
        
        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            
            if u in visited:
                continue
                
            visited.add(u)
            total_cost += cost
            
            x1, y1 = points[u]
            
            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, v))
                    
        return total_cost
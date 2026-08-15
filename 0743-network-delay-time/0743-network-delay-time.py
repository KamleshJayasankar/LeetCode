from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
            
        min_heap = [(0, k)]
        visited = set()
        max_time = 0
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if node in visited:
                continue
                
            visited.add(node)
            max_time = time
            
            
            if len(visited) == n:
                return max_time
                
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))
                    
        return max_time if len(visited) == n else -1
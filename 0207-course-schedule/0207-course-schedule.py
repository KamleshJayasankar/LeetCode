from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1
            
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        completed_courses = 0
        
        while queue:
            node = queue.popleft()
            completed_courses += 1
            
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
       
        return completed_courses == numCourses
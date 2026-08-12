class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visit, prev_height):
            if (
                (r, c) in visit 
                or r < 0 or r >= ROWS 
                or c < 0 or c >= COLS 
                or heights[r][c] < prev_height
            ):
                return
                
            visit.add((r, c))
            
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])           
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])  
            
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])          
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) 
            
        return list(pacific & atlantic)
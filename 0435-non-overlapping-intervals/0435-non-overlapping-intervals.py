class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        prev_end = float("-inf")
        
        for start, end in intervals:
            if start < prev_end:
                removals += 1
            else:
                prev_end = end
                
        return removals
# Last updated: 2/9/2026, 9:53:56 PM
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        # consts for row and col
        ROW = len(heights)
        COL = len(heights[0])
        
        # directions array
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        # min heap
        min_heap = [] #distance, row, col
        heapq.heapify(min_heap)
        min_heap.append((0, 0, 0))
        
        # to mark visited nodes
        visited = set()
        
        while min_heap:
            dist, row, col = heapq.heappop(min_heap)
            
            if ((row, col) in visited):
                continue
            
            if row == ROW - 1 and col == COL - 1:
                return dist
            
            visited.add((row, col))
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                
                if (new_row < 0 
                    or new_row >= ROW
                    or new_col < 0 
                    or new_col >= COL):
                    continue
                
                new_dist = abs(heights[new_row][new_col] - heights[row][col])
                heapq.heappush(min_heap, (max(new_dist, dist), new_row, new_col))
            
        
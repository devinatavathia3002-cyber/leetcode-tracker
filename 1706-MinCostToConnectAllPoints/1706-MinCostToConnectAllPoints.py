# Last updated: 2/9/2026, 9:53:58 PM
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # what do i need
        visited = set()
        point_lengths = defaultdict(list)
        cost = 0
        
        N = len(points)
        
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                distance = abs(x2 - x1) + abs(y2 - y1)
                
                point_lengths[i].append((distance, j))
                point_lengths[j].append((distance, i))
                
        # time to actually run Prim's (LOL)
        heapTime = [[0, 0]]
        heapq.heapify(heapTime)
        
        while len(visited) < N and heapTime:
            weight, vertex = heapq.heappop(heapTime)
            if vertex in visited:
                continue
            cost += weight
            visited.add(vertex)
            
            for value in point_lengths[vertex]:
                curr_x, curr_y = value
                if curr_y in visited:
                    continue
                heapq.heappush(heapTime, [curr_x, curr_y])

        
        return cost
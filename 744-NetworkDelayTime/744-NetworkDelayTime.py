# Last updated: 2/9/2026, 9:54:53 PM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visited = set()
        min_heap = [[0, k]]
        heapq.heapify(min_heap)
        
        t = 0
        
        # setup adjacency list
        node_times = defaultdict(list)
        for i in range(len(times)):
            start, end, weight = times[i]
            node_times[start].append((weight, end))
        
        
        while min_heap and len(visited) < n:
            weight1, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            t = max(t, weight1)
            visited.add(node)
            
            for val in node_times[node]:
                weight2, curr_val = val
                if curr_val not in visited:
                    heapq.heappush(min_heap, [weight1 + weight2, curr_val])
        
        return t if len(visited) == n else -1
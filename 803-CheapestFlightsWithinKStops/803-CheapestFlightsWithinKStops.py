# Last updated: 2/9/2026, 9:54:39 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # now let's do this conventionally (with bellman-ford algo)
        
        if src == dst:
            return 0

        INF = float('inf')
        prev = [INF] * n
        curr = [INF] * n
        prev[src] = 0

        for i in range(1, k + 2):  
            curr = prev[:] 
            for u, v, cost in flights:
                if prev[u] != INF:
                    curr[v] = min(curr[v], prev[u] + cost)
            prev = curr 

        return prev[dst] if prev[dst] != INF else -1

        
        
        # let's do SPFA first (with cycle detection for funsies)
        
#         if src == dst:
#             return 0
        
#         # adjacency list setup
#         graph = defaultdict(list)
#         for i in range(len(flights)):
#             source, dest, price = flights[i]
#             graph[source].append((dest, price))
        
#         # queue will have vals with the source, price, number of stops
#         queue = deque()
#         queue.append([src, 0, 0])
        
#         # destination array, node & corresponding price
#         destination = [float('inf')] * n
#         destination[src] = 0
        
#         while queue:
#             loc, cost, num_stops = queue.popleft()
#             if num_stops > k:
#                 continue
            
#             for dest, price in graph[loc]:
#                 if cost + price < destination[dest]:
#                     destination[dest] = cost + price
#                     queue.append([dest, cost + price, num_stops + 1])
        
#         return destination[dst] if destination[dst] != float('inf') else -1
            
            
        
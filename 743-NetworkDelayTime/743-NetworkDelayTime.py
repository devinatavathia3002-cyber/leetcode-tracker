# Last updated: 6/12/2026, 4:43:13 PM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        
4        visited = set()
5        path = defaultdict(list)
6
7        # from/to weight mapping
8        for time in times:
9            u, v, w = time
10            path[u].append((v, w))
11        
12        minHeap = []
13        t = 0
14
15        heapq.heappush(minHeap, (0, k))
16
17        while len(minHeap) > 0 and len(visited) < n:
18            weight, curr = heapq.heappop(minHeap)
19            if curr in visited:
20                continue
21            visited.add(curr)
22            t = weight # cumulative weight
23
24            for outgoing in path[curr]:
25                end, w = outgoing
26                if end not in visited:
27                    heapq.heappush(minHeap, (weight + w, end))
28                else:
29                    continue
30
31        return t if len(visited) == n else -1
32        
33
34
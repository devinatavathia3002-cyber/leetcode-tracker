# Last updated: 5/6/2026, 9:11:26 PM
1class Solution:
2    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
3        
4        intervals.sort()
5        index = 0 # interval index
6        res = {} # map query to length
7        minHeap = []
8
9        for q in sorted(queries):
10            
11            while index < len(intervals) and intervals[index][0] <= q:
12                l, r = intervals[index]
13                heapq.heappush(minHeap, [r - l + 1, r])
14                index += 1
15            
16            while minHeap and minHeap[0][1] < q:
17                heapq.heappop(minHeap)
18            
19            res[q] = minHeap[0][0] if minHeap else -1
20        
21        output = []
22        for q in queries:
23            output.append(res[q])
24        
25        return output
# Last updated: 6/7/2026, 4:21:30 PM
1class MedianFinder:
2
3    def __init__(self):
4        self.minHeap = []
5        self.maxHeap = []
6
7    def addNum(self, num: int) -> None:
8        if self.minHeap and num >= self.minHeap[0]:
9            heapq.heappush(self.minHeap, num)
10        else:
11            heapq.heappush(self.maxHeap, -1 * num)
12        
13        # rebalance if needed
14        difference = abs(len(self.minHeap) - len(self.maxHeap))
15        if difference > 1:
16            if len(self.maxHeap) > len(self.minHeap):
17                heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
18            if len(self.maxHeap) < len(self.minHeap):
19                heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
20
21    def findMedian(self) -> float:
22        if len(self.minHeap) == len(self.maxHeap):
23            return (self.minHeap[0] + (-1 * self.maxHeap[0])) / 2
24        elif len(self.minHeap) > len(self.maxHeap):
25            return self.minHeap[0]
26        else:
27            return -1 * self.maxHeap[0]
28        
29        
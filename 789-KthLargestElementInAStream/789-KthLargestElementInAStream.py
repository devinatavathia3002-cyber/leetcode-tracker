# Last updated: 2/9/2026, 9:54:42 PM
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.grades = nums
        self.topK = k
        heapq.heapify(self.grades)
        
        while len(self.grades) > self.topK:
            heapq.heappop(self.grades)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.grades, val)
        if len(self.grades) > self.topK:
            heapq.heappop(self.grades)
        return self.grades[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
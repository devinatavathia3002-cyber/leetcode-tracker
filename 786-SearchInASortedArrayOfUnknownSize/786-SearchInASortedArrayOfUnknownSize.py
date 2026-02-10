# Last updated: 2/9/2026, 9:54:43 PM
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        # set boundaries
        
        left = 0
        right = 1
        
        while target > reader.get(right):
            right = right * 2
        
        
        # perform binary search        
        while left <= right:
            
            mid = ((right - left) // 2) + left
            
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
         
# Last updated: 2/9/2026, 9:54:22 PM
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) <= 2:
            return False
        
        beg = 1
        
        # check increasing
        while beg < len(arr) and arr[beg] > arr[beg - 1]:
            beg += 1        
        
        if beg == (len(arr)) or beg == 1:
            return False
        
        # check decreasing
        end = beg
        while end < len(arr):
            if arr[end] >= arr[end - 1]:
                return False
            end += 1
        
        return True
        
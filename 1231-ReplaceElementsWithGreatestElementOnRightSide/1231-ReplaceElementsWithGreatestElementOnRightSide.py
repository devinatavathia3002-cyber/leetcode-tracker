# Last updated: 2/9/2026, 9:54:10 PM
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maximum = -1
        n = len(arr) - 1
        
        while n >= 0:
            curr = arr[n]
            arr[n] = maximum
            maximum = max(maximum, curr)
            
            n -= 1
        
        return arr
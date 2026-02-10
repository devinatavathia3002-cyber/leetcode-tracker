# Last updated: 2/9/2026, 9:54:12 PM
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        zeroesCounter = 0
        n = len(arr)
        
        for i in range(len(arr)):
            if arr[i] == 0:
                zeroesCounter += 1
        
        for i in range(n - 1, -1, -1):
            if (i + zeroesCounter) < n:
                arr[i + zeroesCounter] = arr[i]
            
            if arr[i] == 0:
                zeroesCounter -= 1
                if (i + zeroesCounter) < n:
                    arr[i + zeroesCounter] = 0
                    
                
        
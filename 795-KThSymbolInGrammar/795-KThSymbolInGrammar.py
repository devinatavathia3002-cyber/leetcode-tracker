# Last updated: 2/9/2026, 9:54:40 PM
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        left = 1
        right = 2 ** (n - 1)
        
        count = 0
        
        for i in range(n - 1):
            
            mid = (left + right) // 2
            
            if k <= mid:
                right = mid
            
            else:
                left = mid + 1
                if count:
                    count = 0
                else:
                    count = 1
                
        return count
            
        
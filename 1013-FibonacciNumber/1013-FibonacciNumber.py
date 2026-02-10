# Last updated: 2/9/2026, 9:54:21 PM
class Solution:
    def fib(self, n: int) -> int:
        
        cache = {}
        
        def recurse(n):
            if n < 2:
                return n

            if n in cache:
                return cache[n]

            else:
                returnVal = self.fib(n - 1) + self.fib(n - 2)

            cache[n] = returnVal
            return returnVal    
        
        return recurse(n)
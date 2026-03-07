# Last updated: 3/7/2026, 1:03:35 PM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        l, r = 0, len(arr) - k
4        
5        while l < r:
6            m = ((r - l) // 2) + l # right-biased midpoint
7            
8            if x - arr[m] <= arr[m + k] - x:
9                r = m
10            else:
11                l = m + 1
12                
13        return arr[l:l+k]
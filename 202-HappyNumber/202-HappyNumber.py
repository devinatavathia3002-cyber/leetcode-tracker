# Last updated: 5/31/2026, 2:10:17 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        seen = []
4        newVal = n
5
6        while newVal not in seen and newVal != 1:
7            nextVal = 0
8            seen.append(newVal)
9            while newVal > 0:
10                last = newVal % 10
11                newVal = newVal // 10
12
13                nextVal += (last * last) 
14            newVal = nextVal
15        
16        if newVal == 1:
17            return True
18        return False
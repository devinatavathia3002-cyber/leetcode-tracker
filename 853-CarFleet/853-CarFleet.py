# Last updated: 2/22/2026, 3:25:41 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        
4        together = sorted(zip(position, speed), reverse = True)
5
6        stack = []
7
8        for i in range(len(together)):
9            distance = (target - together[i][0]) / together[i][1]
10
11            if not stack or stack[-1] < distance:
12                stack.append(distance)
13            
14        return len(stack)
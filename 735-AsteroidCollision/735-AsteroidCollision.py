# Last updated: 2/21/2026, 11:51:55 AM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        
4        stack = []
5
6        for rock in asteroids:
7            
8            while stack and rock < 0 and stack[-1] > 0:
9                top = stack[-1]
10                if abs(top) > abs(rock):
11                    rock = 0
12                elif abs(top) < abs(rock):
13                    stack.pop()
14                else:
15                    stack.pop()
16                    rock = 0
17            
18            if rock:
19                stack.append(rock)
20        
21        return stack
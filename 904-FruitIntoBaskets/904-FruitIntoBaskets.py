# Last updated: 8/24/2026, 8:57:11 PM
1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        #[1, 2, 1, 1, 1, 3, 1]
4        num1, num2 = -1, -1
5        last1, last2 = -1, -1
6
7        longest = 0
8        l, r = 0, 0
9
10        while r < len(fruits):
11            curr = fruits[r]
12            if curr != num1 and curr != num2:
13                if num1 == -1:
14                    num1 = curr
15                    last1 = r
16                elif num2 == -1:
17                    num2 = curr
18                    last2 = r
19                else:
20                    longest = max(longest, r - l)
21                    smallest = min(last1, last2)
22                    l = smallest + 1
23                    if smallest == last1:
24                        num1 = curr
25                        last1 = r
26                    else:
27                        num2 = curr
28                        last2 = r
29            elif curr == num1:
30                last1 = r
31            else:
32                last2 = r
33            
34            r += 1
35        
36        longest = max(longest, r - l)
37        return longest
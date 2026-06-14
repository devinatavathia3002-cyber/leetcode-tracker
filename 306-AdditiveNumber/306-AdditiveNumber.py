# Last updated: 6/14/2026, 12:49:42 AM
1class Solution:
2    def isAdditiveNumber(self, num: str) -> bool:
3        
4        if len(num) < 3:
5            return False
6
7        def additive(first, second, remaining):
8            if len(remaining) == 0:
9                return True
10            
11            total = first + second
12            if remaining.startswith(str(total)):
13                first = second
14                second = total
15                if additive(first, second, remaining[len(str(total)):]):
16                    return True
17
18            return False
19
20        # brute force starting two numbers
21        for s in range(1, len(num)):
22            for e in range(s + 1, len(num)):
23                first = num[:s]
24                second = num[s:e]
25
26                if len(first) > 1 and int(first[0]) == 0:
27                    continue
28                if len(second) > 1 and int(second[0]) == 0:
29                    continue
30                
31                print(num[e:])
32 
33                if additive(int(first), int(second), num[e:]):
34                    return True
35        
36        return False
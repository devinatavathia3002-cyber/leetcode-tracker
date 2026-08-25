# Last updated: 8/24/2026, 10:37:49 PM
1class Solution:
2    def decrypt(self, code: List[int], k: int) -> List[int]:
3        n = len(code)
4        newC = [0] * n
5
6        if k == 0:
7            return newC
8        elif k < 0:
9            num = abs(k)
10            for i in range(len(code)):
11                total = 0
12                for j in range(1, num + 1):
13                    index = i - j
14                    total += code[index % n]
15                newC[i] = total
16        else:
17            num = abs(k)
18            for i in range(len(code)):
19                total = 0
20                for j in range(1, num + 1):
21                    index = i + j
22                    total += code[index % n]
23                newC[i] = total
24
25        return newC
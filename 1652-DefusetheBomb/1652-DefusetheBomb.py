# Last updated: 8/24/2026, 11:19:02 PM
1class Solution:
2    def decrypt(self, code: List[int], k: int) -> List[int]:
3        n = len(code)
4        newC = [0] * n
5
6        if k == 0:
7            return newC
8        elif k < 0:
9            num = abs(k)
10            total = 0
11            for j in range(1, num + 1):
12                total += code[-j % n]
13            for i in range(len(code)):
14                newC[i] = total
15                total += code[i]
16                total -= code[(i - num) % n]
17        else:
18            num = abs(k)
19            total = 0
20            for j in range(1, num + 1):
21                total += code[j % n]
22            for i in range(len(code)):
23                newC[i] = total
24                if i < len(code) - 1:
25                    total -= code[i + 1]
26                    total += code[(i + 1 + k) % n]
27
28        return newC
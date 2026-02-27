# Last updated: 2/27/2026, 12:47:00 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        
4        length = min(len(word1), len(word2))
5
6        w1 = 0
7        w2 = 0
8
9        output = ""
10        loop = 0
11
12        while w1 < length and w2 < length:
13            if loop % 2 == 0:
14                output += word1[w1]
15                w1 += 1
16            else:
17                output += word2[w2]
18                w2 += 1
19            
20            loop += 1
21
22        if w2 < len(word2):
23            output += word2[w2:len(word2)]
24        if w1 < len(word1):
25            output += word1[w1:len(word1)]
26        
27        return output
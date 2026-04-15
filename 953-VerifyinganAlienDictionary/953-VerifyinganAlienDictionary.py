# Last updated: 4/14/2026, 7:26:38 PM
1class Solution:
2    def isAlienSorted(self, words: List[str], order: str) -> bool:
3        
4        pos = {}
5        for index, letter in enumerate(order):
6            pos[letter] = index
7        
8        for i in range(len(words) - 1):
9            w1 = words[i]
10            w2 = words[i + 1]
11
12            for c in range(len(w1)):
13                if c >= len(w2):
14                    return False
15                if w1[c] != w2[c]:
16                    if pos[w1[c]] > pos[w2[c]]:
17                        return False
18                    break
19        return True
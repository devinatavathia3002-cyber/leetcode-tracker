# Last updated: 7/30/2026, 10:31:32 PM
1class Solution:
2    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
3        smallest = len(wordsDict)
4        w1 = len(wordsDict)
5        w2 = (len(wordsDict) * -1)
6        for i in range(len(wordsDict)):
7            curr = wordsDict[i]
8            if curr == word1:
9                w1 = i
10            if curr == word2:
11                w2 = i
12            smallest = min(smallest, abs(w1 - w2))
13        return smallest
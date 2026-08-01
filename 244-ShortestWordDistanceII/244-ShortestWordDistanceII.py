# Last updated: 8/1/2026, 3:14:39 PM
1class WordDistance:
2
3    def __init__(self, wordsDict: List[str]):
4        self.dictionary = defaultdict(list)
5        self.wordsDict = wordsDict
6        for i in range(len(wordsDict)):
7            self.dictionary[wordsDict[i]].append(i)
8
9    def shortest(self, word1: str, word2: str) -> int:
10        arr1 = self.dictionary[word1]
11        arr2 = self.dictionary[word2]
12
13        l1, l2 = 0, 0
14        minimum = len(self.wordsDict)
15
16        while l1 < len(arr1) and l2 < len(arr2):
17            pt1, pt2 = arr1[l1], arr2[l2]
18            minimum = min(minimum, abs(pt1 - pt2))
19
20            if pt1 < pt2:
21                l1 += 1
22            else:
23                l2 += 1
24        
25        return minimum
26
27
28# Your WordDistance object will be instantiated and called as such:
29# obj = WordDistance(wordsDict)
30# param_1 = obj.shortest(word1,word2)
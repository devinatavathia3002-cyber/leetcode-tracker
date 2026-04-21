# Last updated: 4/20/2026, 9:22:18 PM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        
4        if endWord not in wordList:
5            return 0
6
7        visit = set()
8        q = deque()
9        adj = defaultdict(list)
10        layer = 0
11
12        for word in wordList:
13            for letter in range(len(word)):
14                key = word[:letter] + "*" + word[letter + 1:]
15                adj[key].append(word)
16        
17        # initialize queue
18        for letter in range(len(beginWord)):
19            key = beginWord[:letter] + "*" + beginWord[letter + 1:]
20            q.append(key)
21        
22        while q:
23            length = len(q)
24            layer += 1 # layer increment
25            for i in range(length):
26                pattern = q.popleft()
27                visit.add(pattern) # visit tracker
28                for index, word in enumerate(adj[pattern]):
29                    if word == endWord:
30                        return layer + 1
31                    for letter in range(len(word)):
32                        key = word[:letter] + "*" + word[letter + 1:]
33                        if key not in visit:
34                            q.append(key)
35                    
36        return 0
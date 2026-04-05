# Last updated: 4/5/2026, 12:01:51 AM
1class TrieNode:
2
3    def __init__(self):
4        self.children = {}
5        self.endOfWord = False 
6
7class WordDictionary:
8
9    def __init__(self):
10        self.root = TrieNode()
11
12    def addWord(self, word: str) -> None:
13        curr = self.root
14
15        for c in word:
16            if c not in curr.children:
17                curr.children[c] = TrieNode()
18            curr = curr.children[c]
19
20        curr.endOfWord = True
21
22    def search(self, word: str) -> bool:
23        curr = self.root
24
25        def dfs(curr, index):
26            for i in range(index, len(word)):
27                letter = word[i]
28                if letter == '.':
29                    for c in curr.children:
30                        if dfs(curr.children[c], i + 1):
31                            return True
32                    return False
33                else:
34                    if letter not in curr.children:
35                        return False
36                    curr = curr.children[letter]
37            return curr.endOfWord
38        
39        return dfs(curr, 0)
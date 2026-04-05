# Last updated: 4/4/2026, 10:28:04 PM
1class TrieNode:
2
3    def __init__(self):
4        self.children = {}
5        self.endOfWord = False
6
7class Trie:
8
9    def __init__(self):
10        self.root = TrieNode()
11        
12    def insert(self, word: str) -> None:
13        curr = self.root
14        for char in word:
15            if char not in curr.children:
16                curr.children[char] = TrieNode()
17            curr = curr.children[char]
18        curr.endOfWord = True
19
20    def search(self, word: str) -> bool:
21        curr = self.root
22        for char in word:
23            if char not in curr.children:
24                return False
25            curr = curr.children[char]
26        return curr.endOfWord
27
28    def startsWith(self, prefix: str) -> bool:
29        curr = self.root
30        for char in prefix:
31            if char not in curr.children:
32                return False
33            curr = curr.children[char]
34        return True
35        
36        
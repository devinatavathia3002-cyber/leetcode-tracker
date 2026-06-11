# Last updated: 6/10/2026, 7:36:33 PM
1class TrieNode:
2    def __init__(self):
3        self.endOfWord = False
4        self.children = {}
5    def addWord(self, word):
6        curr = self
7        for c in word:
8            if c not in curr.children:
9                curr.children[c] = TrieNode()
10            curr = curr.children[c]
11        curr.endOfWord = True
12
13class Solution:
14    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
15        ROWS = len(board)
16        COLS = len(board[0])
17
18        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
19        visited, output = set(), set()
20
21        root = TrieNode()
22        for word in words:
23            root.addWord(word)
24
25        def dfs(r, c, node, word):
26            char = board[r][c]
27            word += char
28
29            nextNode = node.children[char]
30
31            if len(output) == len(words):
32                return
33            if nextNode.endOfWord:
34                output.add(word)
35            
36            for cord in directions:
37                x, y = cord
38                newR, newC = x + r, y + c
39                if 0 <= newR < ROWS and 0 <= newC < COLS and (newR, newC) not in visited and board[newR][newC] in nextNode.children:
40                    visited.add((newR, newC))
41                    dfs(newR, newC, nextNode, word)
42                    visited.remove((newR, newC))
43
44        for r in range(ROWS):
45            for c in range(COLS):
46                if board[r][c] in root.children:
47                    visited.add((r, c))
48                    dfs(r, c, root, "")
49                    visited.remove((r, c))
50
51        return list(output)
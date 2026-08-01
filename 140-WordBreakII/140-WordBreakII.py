# Last updated: 8/1/2026, 1:27:12 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
3        output = []
4
5        def recurse(i, phrase):
6            if i >= len(s):
7                output.append(phrase[:len(phrase) - 1])
8                return
9            
10            for word in wordDict:
11                length = len(word)
12                if (i + length) <= len(s) and s[i:i + length] == word:
13                    recurse(i + length, phrase + word + " ")
14            
15            return 
16            
17        recurse(0, "")
18        return output
# Last updated: 8/26/2026, 6:51:28 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        vowelCt = 0
4        currCt = 0
5        l, r = 0, 0
6
7        vowels = ('a', 'e', 'i', 'o', 'u')
8
9        while r < len(s):
10            curr = s[r]
11            length = (r - l + 1)
12            if curr in vowels:
13                currCt += 1
14            if length == k:
15                vowelCt = max(vowelCt, currCt)
16                if s[l] in vowels:
17                    currCt -= 1
18                l += 1
19            r += 1
20
21        return vowelCt
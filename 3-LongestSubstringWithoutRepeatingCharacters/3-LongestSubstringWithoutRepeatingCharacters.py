# Last updated: 2/13/2026, 12:05:05 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3
4        letters = set()
5        left = 0
6        right = 0
7        longest = 0
8
9        while right < len(s):
10            if s[right] not in letters:
11                letters.add(s[right])
12            else:
13                while s[left] != s[right]:
14                    letters.remove(s[left])
15                    left += 1
16                left += 1
17
18            print(right)
19            longest = max(longest, right - left + 1)
20            right += 1
21
22        return longest
23
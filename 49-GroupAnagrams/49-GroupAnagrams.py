# Last updated: 2/9/2026, 11:16:05 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3
4        # using a character map
5
6        d = defaultdict(list)
7        for i in range(len(strs)):
8            chars = [0] * 26
9            for s in strs[i]:
10                chars[ord(s) - ord('a')] += 1
11            d[tuple(chars)].append(strs[i])
12        
13        return list(d.values())
14            
15        
# Last updated: 7/4/2026, 5:39:55 PM
1class Solution:
2    def numTilePossibilities(self, tiles: str) -> int:
3        count = defaultdict(int)
4        for tile in tiles:
5            count[tile] += 1
6        
7        def findOptions(sub):
8            if len(sub) == len(tiles):
9                return 0
10            
11            res = 0
12            for key in count.keys():
13                if count[key] > 0:
14                    sub.append(key)
15                    count[key] -= 1
16                    res += (1 + findOptions(sub))
17                    sub.pop()
18                    count[key] += 1
19                else:
20                    continue
21            
22            return res
23        
24        return findOptions([])
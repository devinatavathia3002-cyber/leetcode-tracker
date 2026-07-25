# Last updated: 7/25/2026, 10:49:32 AM
1class Solution:
2    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
3        output = [0] * len(spells)
4        potions = sorted(potions)
5
6        for i in range(len(spells)):
7            spell = spells[i]
8            index = len(potions)
9            l, r = 0, len(potions) - 1
10
11            while l <= r:
12                mid = ((r - l) // 2) + l # acc for int overflow
13                if (potions[mid] * spell) >= success:
14                    index = min(mid, index)
15                    r = mid - 1
16                else:
17                    l = mid + 1
18            
19            output[i] = len(potions) - index
20
21        return output